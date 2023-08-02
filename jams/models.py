from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Artist(models.Model):
    name = models.CharField(max_length=50)
    genre_id = models.ManyToManyField('Genre')

class Album(models.Model):
    name = models.CharField(max_length=50)
    artist_id = models.ManyToManyField('Artist')

class Song(models.Model):
    name = models.CharField(max_length=50)
    album_id = models.ManyToManyField('Album')