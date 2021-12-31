# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Robobusters
"""

from django.urls import path, re_path
from apps.attendance import views
def repath_func(request):
    from django.http import HttpResponseRedirect


    return HttpResponseRedirect(request.path_info)
urlpatterns = [

    # The home page
    path('', views.stdAttIndex, name='attendance'),
    
    
    # Matches any html file
    path('list/', views.stdAttShowList,name='att-list'),
    
    
    
]
