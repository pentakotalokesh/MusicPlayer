# Generated by Django 4.2.2 on 2023-06-16 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_alter_song_thumbnail_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
