from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField( max_length=255)
    original_title = models.CharField( max_length=255)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    overview = models.TextField()
    original_language = models.CharField( max_length=255)
    poster_path = models.CharField( max_length=255)
    backdrop_path = models.CharField( max_length=255)
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    like_users = models.ManyToManyField(get_user_model(), related_name="like_movies")