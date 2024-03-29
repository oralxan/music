# Generated by Django 4.2.8 on 2024-03-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126, verbose_name='name of the album')),
                ('about', models.TextField(blank=True, null=True, verbose_name='about of the album')),
                ('released_date', models.DateField(verbose_name='released_date of the album')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
    ]
