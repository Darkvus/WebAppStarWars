from django.db import models

from StarWarsApp.models.pelicula import Pelicula


class Personaje(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    height = models.CharField(max_length=7)
    mass = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=10)
    eye_color = models.CharField(max_length=10)
    birth_year = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'),
                                                      ('F', 'Femenino'),
                                                      ('N/A', 'N/a')])
    image = models.CharField(max_length=50, blank=True)
    url_API = models.CharField(max_length=50, blank=True)
    peliculas = models.ManyToManyField(Pelicula, null=True)

    class Meta:
        verbose_name = ("Personaje")
        verbose_name_plural = ("Personajes")

    def __str__(self):
        return self.nombre
