from __future__ import unicode_literals

from django.db import models

# Create your models here.

class fitdata(models.Model):
    date = models.DateField(default=None)
    steps = models.IntegerField()
    distance = models.IntegerField()
    weight = models.IntegerField()
    fat = models.IntegerField()