from rest_framework import serializers
from albums.models import Album, AlbumSing, Sing, Singer
from django.shortcuts import get_object_or_404

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
    """Поле для id в модели связей ингредиентов и рецептов."""
    def to_representation(self, value):
        """Предоставить значение без преобразования."""
        return value

    def to_internal_value(self, data):
        """Проверить наличие ингредиента и вернуть id."""
        get_object_or_404(Sing, id=data)
        return data


class AlbumSingSerializers(serializers.ModelSerializer):
    """Сериализатор для связи альбома, песни и порядкового номера."""
    id = IdSingField(source='sing.id')
    name = serializers.ReadOnlyField(source='sing.name')

    class Meta:
        model = AlbumSing
        fields = ('id', 'name', 'number_sing')
        read_only_fields = ('name', )


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для альбомов."""
    sings = AlbumSingSerializers(
        many=True,
        source='albumsing_set'
    )
    singer = SingerSerializer()

    class Meta:
        model = Album
        fields = ('name', 'year', 'singer', 'sings')

    # def create(self, validated_data):
    #     return super().create(validated_data)


# class AlbumWriteSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Album
#         fields = ('name', 'year', 'singer', 'sings')
