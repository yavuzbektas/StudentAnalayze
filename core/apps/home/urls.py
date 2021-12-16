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
    path('maps-google.html', views.index, name='home'),
    
    
    # Matches any html file
    path('profil.html', views.profilUpdate, name='users-edit'),
    path('view/<int:pk>', views.profilView, name='users-view'),
    path('usr-ogretmenler.html', views.profilShowList,name='kullanicilar'),
    path('delete/<int:pk>',views.profilDelete, name='delete'),
    path('yetki/<int:pk>',views.issuperUser, name='yetki'),
    
    #re_path(r'^.*\.*', views.pages, name='pages'),
    
]
