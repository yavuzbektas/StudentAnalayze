from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# Register your models here.

from .models import LessonPeriods
admin.site.register(LessonPeriods)