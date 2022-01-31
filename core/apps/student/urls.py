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
    path('std-profile.html', views.studentUpdate, name='student-edit'),
    path('view/<int:pk>', views.studentView, name='student-view'),
    path('update/<int:pk>', views.studentUpdate, name='student-update'),
    path('add/', views.studentAdd, name='student-add'),
    path('delete/<int:pk>',views.studentDelete, name='student-delete'),
    path('list/', views.StudentListView.as_view(),name='student-list'),
    path('parent/update/<int:pk>', views.parentUpdate, name='parent-Update'),
    path('parent/add',views.parentAdd,name='parentAdd'),
    path('import/', views.studentImport,name='student-import'),
    path('export/', views.export,name='student-export'),
]
