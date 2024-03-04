from rest_framework.viewsets import ModelViewSet

from .models import Music
from.serializers import MusicSerializer
class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    