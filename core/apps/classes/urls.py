# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Robobusters
"""

from django.urls import path, re_path
from apps.classes import views
def repath_func(request):
    from django.http import HttpResponseRedirect


    return HttpResponseRedirect(request.path_info)
urlpatterns = [

    # The home page
    path('', views.classesIndex, name='classes'),
    
    
    # Matches any html file
    path('classes.html', views.classesUpdate, name='classes-edit'),
    path('StudentListUpdateView/<int:pk>', views.StudentListUpdateView, name='StudentListUpdateView'),
    path('view/<int:pk>', views.classesView, name='classes-view'),
    path('list/', views.classesShowList,name='classes-list'),
    path('delete/<int:pk>',views.classesDelete, name='classes-delete'),
    path('page-blank.html',views.StudentListDetailView.as_view(), name='detail'),
    path('list/<str:filterBy>/<str:filterValue>', views.classesShowListFiltered,name='classes-list-filtered') , ]
    
    