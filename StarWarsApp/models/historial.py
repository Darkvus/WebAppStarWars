from django.db import models
from datetime import datetime as dt


class Historial(models.Model):
    url = models.CharField(max_length=200)
    date = models.DateTimeField(default=dt.now(), blank=True)