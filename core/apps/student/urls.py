# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
def repath_func(request):
    from django.http import HttpResponseRedirect


    return HttpResponseRedirect(request.path_info)
urlpatterns = [

    # The home page
    path('student/', views.index, name='student'),
    
    
    # Matches any html file
    path('student/profil.html', views.studentUpdate, name='student-edit'),
    path('student/view/<int:pk>', views.studentView, name='student-view'),
    path('student/view/list', views.studentShowList,name='student-list'),
    path('student/delete/<int:pk>',views.studentDelete, name='student-delete'),
    
    
]
