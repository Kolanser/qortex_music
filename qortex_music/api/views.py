from rest_framework.viewsets import ModelViewSet
from albums.models import Album, Sing, Singer
from .serializers import AlbumSerializer, SingSerializer, SingerSerializer


class SingViewSet(ModelViewSet):
    queryset = Sing.objects.all()
    serializer_class = SingSerializer


class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
