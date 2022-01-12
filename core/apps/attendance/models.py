
from django.db import models

from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField,ForeignKey,ManyToManyField
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField, DateField, IntegerField, NullBooleanField, TextField
from django.contrib.auth.models import User
from apps.student.models import Student,StudentList
from apps.home.models import Session,Period
# Create your models here.
class LessonPeriods(models.Model):
    id = AutoField(primary_key=True)
    lessCount = models.IntegerField(default="1")
    lessName=models.CharField(max_length=15,default="1.Ders",verbose_name="Ders No")
    lesPeriod=models.CharField(max_length=15,default="09:30-10:10")
    session=models.ForeignKey(Session,on_delete=models.CASCADE,default=2)
    periods=models.ForeignKey(Period,on_delete=models.CASCADE,default=2)
    def __str__(self):
      return self.lessName + "-" + self.lesPeriod 

class DailyAttendance(models.Model):
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    periods=models.ForeignKey(Period,on_delete=models.CASCADE)
    lesPeriod=models.ForeignKey(LessonPeriods, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    day=models.DateField(auto_now=True) 
    def __str__(self):
      return self.session.session + "-" + self.periods.period + str(self.day) +"/ Ders Saati: " + self.lesPeriod.lesPeriod +"/ Sınıf:" +  self.student.firstName +" " +self.student.lastName 