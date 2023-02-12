from rest_framework import serializers
from albums.models import Album, AlbumSing, Sing, Singer
from django.shortcuts import get_object_or_404
from django.db import transaction


class SingSerializer(serializers.ModelSerializer):
    """Сериализатор для песен."""

    class Meta:
        model = Sing
        fields = ('id', 'name', )
        read_only_fields = ('id', )


class SingerSerializer(serializers.ModelSerializer):
    """Сериализатор для исполнителей."""

    class Meta:
        model = Singer
        fields = ('id', 'name', )
        read_only_fields = ('id', )


class IdSingField(serializers.Field):
    """Поле для id в модели связей альбомов и песен."""
    def to_representation(self, value):
        """Предоставить значение без преобразования."""
        return value

    def to_internal_value(self, data):
        """Проверить наличие песни и вернуть id."""
        get_object_or_404(Sing, id=data)
        return data


class AlbumSingSerializers(serializers.ModelSerializer):
    """Сериализатор для связи альбома, песни и порядкового номера."""
    id_sing = IdSingField(source='sing.id')
    name = serializers.ReadOnlyField(source='sing.name')

    class Meta:
        model = AlbumSing
        fields = ('id_sing', 'name', 'number_sing')
        read_only_fields = ('name', )


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для альбомов."""
    sings = AlbumSingSerializers(
        many=True,
        source='albumsing_set'
    )
    singer = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Singer.objects.all()
    )

    class Meta:
        model = Album
        fields = ('id', 'name', 'year', 'singer', 'sings')

    @transaction.atomic
    def create(self, validated_data):
        """Создание альбома."""
        album_sings = validated_data.pop('albumsing_set')
        album = super().create(validated_data)
        sings_number = []
        for sing in album_sings:
            id = sing['sing'].get('id')
            sings_number.append(
                AlbumSing(
                    album=album,
                    sing=Sing.objects.get(id=id),
                    number_sing=sing.get('number_sing')
                )
            )
        AlbumSing.objects.bulk_create(sings_number)
        return album

    @transaction.atomic
    def update(self, instance, validated_data):
        """Изменение альбома."""
        album_sings = validated_data.pop('albumsing_set')
        album = super().update(instance, validated_data)
        album.sings.clear()
        sings_number = []
        for sing in album_sings:
            id = sing['sing'].get('id')
            sings_number.append(
                AlbumSing(
                    album=album,
                    sing=Sing.objects.get(id=id),
                    number_sing=sing.get('number_sing')
                )
            )
        AlbumSing.objects.bulk_create(sings_number)
        return album

    def validate(self, attrs):
        """Проверка данных."""
        name = attrs.get('name')
        year = attrs.get('year')
        singer = attrs.get('singer')
        if Album.objects.filter(
            name=name,
            year=year,
            singer=singer
        ).exists():
            raise serializers.ValidationError(
                (
                    'Не может быть альбома с таким же'
                    ' названием, годом и исполнителем.'
                )
            )
        return super().validate(attrs)
