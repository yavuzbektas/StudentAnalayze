# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin

# Register your models here.

from .models import JobsTable,ProfilDetay,Session

admin.site.register(JobsTable)
admin.site.register(ProfilDetay)
admin.site.register(Session)
