from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=300)
    original_title = models.CharField(max_length=300)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    overview = models.TextField()
    original_language = models.CharField(max_length=300)
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name = 'movies')

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    # def review_score(self):
    #     return sum(self.reviews.score)/self.reviews.count()