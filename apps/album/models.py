from django.db.models import *
from apps.music.models import Music

class Album(Model):
    name = CharField(
        'name of the album',
        max_length=126
    )
    about = TextField(
        'about of the album',
        null=True,
        blank=True
    )
    music = ManyToManyField(
        Music,
        verbose_name='Music'
    )
    released_date = DateField(
        'released_date of the album',

    )
    def __str__(self):
        return f'{self.name}'
    class Meta:
     verbose_name = 'Album'
     verbose_name_plural = 'Albums'
