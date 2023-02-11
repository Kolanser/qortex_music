from rest_framework import exceptions, serializers
from rest_framework.validators import UniqueValidator
import datetime as dt
from albums.models import Sing, Singer


class SingSerializer(serializers.ModelSerializer):
    """Сериализатор для песен."""

    class Meta:
        model = Sing
        fields = ('id', 'name', )


class SingerSerializer(serializers.ModelSerializer):
    """Сериализатор для исполнителей."""

    class Meta:
        model = Singer
        fields = ('id', 'name', )
