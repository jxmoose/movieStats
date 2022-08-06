import uuid
from django.db import models

# Create your models here.

class Movie(models.Model):
    user_id = models.UUIDField()
    tconst = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null = True, default=None)
    releaseDate = models.DateField()
    watchDate = models.DateField(null = True, default=None)
    numVotes = models.IntegerField(default = 0)
    imdbRating = models.DecimalField(max_digits=4, decimal_places=2, null = True, default=None)

class Directors(models.Model):
    tconst = models.CharField(max_length=20)
    director = models.CharField(max_length=100)

class Writers(models.Model):
    tconst = models.CharField(max_length=20)
    writer = models.CharField(max_length=100)

class Cast(models.Model):
    tconst = models.CharField(max_length=20)
    actor = models.CharField(max_length=100)

class Genres(models.Model):
    tconst = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)