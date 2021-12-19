from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# Register your models here.

from .models import LessonPeriods,DailyAttendance
admin.site.register(LessonPeriods)
admin.site.register(DailyAttendance)
