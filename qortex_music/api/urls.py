from django.urls import include, path
from rest_framework import routers
from .views import (
    SingViewSet,
    SingerViewSet
)

router = routers.DefaultRouter()
router.register('sings', SingViewSet, basename='sing')
router.register('singers', SingerViewSet, basename='singers')

urlpatterns = [
    path('', include(router.urls)),
]