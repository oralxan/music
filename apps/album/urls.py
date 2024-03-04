from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet

router = DefaultRouter()
router.register('album', AlbumViewSet, basename='album')

urlpatterns = []
urlpatterns += router.urls
