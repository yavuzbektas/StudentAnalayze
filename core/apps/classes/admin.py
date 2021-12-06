from django.contrib import admin

# Register your models here.
from .models import Classes,ClassLevels,ClassNames

admin.site.register(Classes)
admin.site.register(ClassLevels)
admin.site.register(ClassNames)
