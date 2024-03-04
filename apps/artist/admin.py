from django.contrib.admin import *
from .models import Artist
@register(Artist)
class AlbumAdmin(ModelAdmin):
    list_display = ('id','fullname','photo')
    list_display_links =  ('id','fullname','photo')
    ordering = ('fullname',)