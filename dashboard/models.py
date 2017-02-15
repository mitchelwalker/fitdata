from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class fitdata(models.Model):
    user = models.ForeignKey(User, unique=True)
    date = models.DateField(auto_now_add=True)
    steps = models.IntegerField()
    distance = models.IntegerField()

class weightdata(models.Model):
    user = models.ForeignKey(User, unique=True)
    date = models.DateField(auto_now_add=True)
    weight = models.IntegerField()
    fat = models.IntegerField()