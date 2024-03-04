from rest_framework.viewsets import ModelViewSet

from .models import Album
from.serializers import AlbumSerializer
class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    