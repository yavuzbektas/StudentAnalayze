from unicodedata import name
from django.db import models
from apps.student.models import StudentList
from apps.home.models import Profil
from apps.attendance.models import LessonPeriods

class Lesson(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=5)
    def __str__(self): 
      return self.code + "-" + self.name

class LessonClassList(models.Model):
    className= models.ForeignKey(StudentList,unique=False, related_name='lesson_classname', on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, related_name='lesson_lesson', on_delete=models.CASCADE)
    teacher=models.ForeignKey(Profil,blank=True, related_name='lesson_profil', on_delete=models.CASCADE)
    def __str__(self): 
      return str(self.className) 

class LessonPlan(models.Model):
    className= models.ForeignKey(LessonClassList,unique=False, related_name='lessonplan_lessonclasslist', on_delete=models.CASCADE)
    lessonPeriods=models.ForeignKey(LessonPeriods, related_name='lessonplan_LessonPeriods', on_delete=models.CASCADE)

    def __str__(self): 
      return self.className