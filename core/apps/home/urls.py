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
    path('', views.index, name='home'),
    
    
    # Matches any html file
    path('profil.html', views.post_update, name='users-edit'),
    path('usr-ogretmenler.html', views.userShow,name='kullanicilar'),
    path('delete/<int:pk>',views.post_delete, name='delete'),
    
    #re_path(r'^.*\.*', views.pages, name='pages'),
    
]
