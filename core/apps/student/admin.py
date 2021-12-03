from django.contrib import admin

# Register your models here.
from .models import Parent,MiddleSchool,Student

admin.site.register(Parent)
admin.site.register(MiddleSchool)
admin.site.register(Student)
