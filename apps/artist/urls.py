from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet

router = DefaultRouter()
router.register('artist', ArtistViewSet, basename='artist')

urlpatterns = []
urlpatterns += router.urls
