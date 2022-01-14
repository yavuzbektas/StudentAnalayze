from unicodedata import name
from django.db import models
from apps.student.models import StudentList
# Create your models here.
"""class StudentList(models.Model):
    className=models.ForeignKey(Classes,on_delete=models.CASCADE)
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    periods=models.ForeignKey(Period,on_delete=models.CASCADE)
    students=models.ManyToManyField(Student,blank=True)
    teachers=models.ManyToManyField(Profil,blank=True,verbose_name="Sınıf Öğretmeni",related_name='teacher')"""

class Lesson(models.Model):
    name=models.CharField(max_length=30)

class LessonClassList(models.Model):
    className=models.ManyToManyField(StudentList,blank=True,verbose_name="Sınıs Adı",related_name='class_name')
    lessons=models.ManyToManyField(Lesson,blank=True,verbose_name="Dersler",related_name='lessonName')