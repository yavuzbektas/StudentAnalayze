
from django.db import models

from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.contrib.auth.models import User


# Create your models here.
class LessonPeriods(models.Model):
    lesPeriod=models.CharField(max_length=15,default="9:30-10:10",unique=True)
    def __str__(self):
      return self.lesPeriod