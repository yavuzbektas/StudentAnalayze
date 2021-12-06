from django.db import models

from apps.home.models import Profil,Session
from django.db.models.fields.related import OneToOneField,ManyToManyField
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, IntegerField, TextField
# Create your models here.
class ClassLevels(models.Model):
    level=models.CharField(default="9",max_length=2,unique=True)
    def __str__(self): 
        return self.level

class ClassNames(models.Model):
    name=models.CharField(default="A",max_length=1,unique=True)
    class Meta:
        ordering = ('name',)
    def __str__(self): 
        return self.name

class Classes(models.Model):
    className=models.ForeignKey(ClassNames,on_delete=models.CASCADE,default="")
    level=models.ForeignKey(ClassLevels,on_delete=models.CASCADE)
    def __str__(self):
        
        return self.level.level+self.className.name

