# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    
    
    # Matches any html file
    path('profil.html',views.userUpdate, name="profil"),
    path('profilRegister.html',views.userAdd , name="profilEkle"),
    path('usr-ogretmenler.html', views.userShow,name='kullanicilar'),
    #re_path(r'^.*\.*', views.pages, name='pages'),
]
