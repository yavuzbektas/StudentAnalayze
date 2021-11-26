# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('usr-ogretmenler.html', views.userShow,name='kullanicilar'),
    path('profil.html',views.userUpdate, name="profil"),
    path('profil.html',views.userAdd , name="profilEkle"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
