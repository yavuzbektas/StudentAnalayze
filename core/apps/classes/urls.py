# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Robobusters
"""

from os import name
from django.shortcuts import redirect
from django.urls import path, re_path
from apps.classes import views
def repath_func(request):
    from django.http import HttpResponseRedirect


    return HttpResponseRedirect(request.path_info)
urlpatterns = [

    # The home page
    path('', views.classesListIndex, name='classes'),
    
    
    # Matches any html file
    path('classes.html', views.classesUpdate, name='classes-edit'),
    path('view/<int:pk>',views.classesListView, name='classesList-view'),
    path('add/<int:classlevelID>/<int:classnameID>',views.classesListAdd, name='classesList-add'),
    path('update/<int:pk>',views.classesListUpdate, name='classesList-update'),
    path('delete/<int:pk>',views.classesListDelete, name='classesList-delete'),
    path('classes/view/<int:pk>', views.classesView, name='classes-view'),
    path('classes/add/<int:classname>', views.classesAdd, name='classes-view'),
    path('classes/update/<int:pk>', views.classesDelete, name='classes-view'),
    path('classes/list/', views.classesShowList,name='classes-list'),
    path('classes/delete/<int:pk>',views.classesDelete, name='classes-delete'),
    path('list/<str:filterBy>/<str:filterValue>', views.classesShowListFiltered,name='classes-list-filtered') ,
    path('StudentListUpdateView/<int:pk>', views.StudentListUpdateView, name='StudentListUpdateView'),
    path('Seat_arrangement/<int:pk>', views.UpdateSeating, name='upd-seating'),
    path('assign/',views.StudentListDetailView.as_view(), name='classes-detail'),
    path('classredirect/<str:pk>',views.classredirect,name ='redirecttoclass'),
    path('class/<int:pk>',views.classlist,name="classlist"),
    path('success/',views.success,name="success")
]
    
    