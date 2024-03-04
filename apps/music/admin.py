from django.contrib.admin import *
from .models import Music
@register(Music)
class MusicAdmin(ModelAdmin):
    list_display = ('id','name','about')
    list_display_links =  ('id','name','about')
    ordering = ('name',)