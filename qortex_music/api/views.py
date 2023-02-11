from rest_framework.viewsets import ModelViewSet
from albums.models import Sing, Singer
from .serializers import SingSerializer, SingerSerializer


class SingViewSet(ModelViewSet):
    queryset = Sing.objects.all()
    serializer_class = SingSerializer


class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
