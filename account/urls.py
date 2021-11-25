# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from apps.polls import views
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('layouts/base.html', login_view, name="login"),
     path('index', views.index, name='index'),
    path('home/login.html', login_view, name="login"),
    path('home/register.html', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),]