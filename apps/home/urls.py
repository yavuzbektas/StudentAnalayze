# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home.views import login_view, register_user
from apps.home import LogoutView, views
from apps.polls import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
  
    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    path("logout/", LogoutView.as_view(), name="logout")
]
