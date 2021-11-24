from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.
class User(models.Model):
    "'username', 'email', 'password1', 'password2'"
    username=models.CharField(max_length=100)
    

