
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AlbumViewSet, SongViewSet

router = DefaultRouter()

router.register('album', AlbumViewSet, basename='album')
router.register('song', SongViewSet, basename='song')

urlpatterns = [
        path('', include(router.urls)),
]
