from django.db.models import *
class Music(Model):
    name = CharField(
        'name of the music',
        max_length=126
    )
    about = TextField(
        'about of the music',
        null=True,
        blank=True
    )
    released_date = DateField(
        'released_date of the music',
        auto_now_add=True

    )
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'