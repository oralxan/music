from django.db.models import *
from apps.music.models import Music
from apps.album.models import Album

class Artist(Model):
    fullname = CharField(
        'fullname of  Artist',
        max_length=126
    )
    date_of_birth = DateField(
        'birth of the Artist',
    )
    albums = ManyToManyField(
       Album,
       verbose_name='Albums'

    )
    songs = ManyToManyField(
       Music,
       verbose_name='musics'
    )
    information = TextField(
       'information of th Artist',
       blank=True,
       null=True
    )
    photo= ImageField(
        'img Artist',
        upload_to='artist-photos/%Y/%m/%d',
    )

    def __str__(self):
        return f'{self.fullname}'
    class Meta:
     verbose_name = 'Arist'
     verbose_name_plural = 'Artists'
