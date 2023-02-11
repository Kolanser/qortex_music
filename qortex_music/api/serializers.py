from rest_framework import exceptions, serializers
from rest_framework.validators import UniqueValidator
import datetime as dt
from albums.models import Sing


class SingSerializer(serializers.ModelSerializer):
    """Сериализатор модели Sing."""

    class Meta:
        model = Sing
        fields = ('name', )