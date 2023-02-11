from django.urls import include, path
from rest_framework import routers
from .views import (
    SingViewSet,
)

router = routers.DefaultRouter()
router.register('sings', SingViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]