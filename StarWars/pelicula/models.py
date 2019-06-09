from django.db import models
from personaje.models import Personaje

class Pelicula(models.Model):
    episode_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=75)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    release_date = models.DateField()
    image = models.CharField(max_length=50, blank=True)
    url_API = models.CharField(max_length=50, blank=True)
    character = models.ForeignKey(Personaje, on_delete=models.CASCADE)
