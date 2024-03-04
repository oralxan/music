from rest_framework.serializers import ModelSerializer
from .models import Music

class MusicSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


        