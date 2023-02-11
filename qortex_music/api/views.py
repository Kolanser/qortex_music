from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from albums.models import Sing
from .serializers import SingSerializer


class SingViewSet(ModelViewSet):
    queryset = Sing.objects.all()
    serializer_class = SingSerializer
