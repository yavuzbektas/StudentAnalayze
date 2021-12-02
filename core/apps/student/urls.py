# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Robobusters
"""

from django.urls import path, re_path
from apps.student import views
def repath_func(request):
    from django.http import HttpResponseRedirect


    return HttpResponseRedirect(request.path_info)
urlpatterns = [

    # The home page
    path('', views.studentIndex, name='student'),
    
    
    # Matches any html file
    path('profil.html', views.studentUpdate, name='student-edit'),
    path('view/<int:pk>', views.studentView, name='student-view'),
    path('list/', views.studentShowList,name='student-list'),
    path('delete/<int:pk>',views.studentDelete, name='student-delete'),
    
    
]
