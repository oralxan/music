from rest_framework.viewsets import ModelViewSet

from .models import Artist
from.serializers import ArtistSerializer
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    