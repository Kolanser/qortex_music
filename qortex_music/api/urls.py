from django.urls import include, path
from rest_framework import routers
from .views import (
    AlbumViewSet,
    SingViewSet,
    SingerViewSet
)

router = routers.DefaultRouter()
router.register('sings', SingViewSet, basename='sing')
router.register('singers', SingerViewSet, basename='singer')
router.register('albums', AlbumViewSet, basename='album')

urlpatterns = [
    path('', include(router.urls)),
]
