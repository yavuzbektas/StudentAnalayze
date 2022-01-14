from django.contrib import admin

# Register your models here.
from .models import Lesson,LessonClassList

admin.site.register(Lesson)
admin.site.register(LessonClassList)

