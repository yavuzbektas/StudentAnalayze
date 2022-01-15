from django.urls import path
from apps.lessons import views
def repath_func(request):
    from django.http import HttpResponseRedirect


    return HttpResponseRedirect(request.path_info)
urlpatterns = [

    
    
    
    path('add/', views.LessonAdd  ,name='LessonAdd'),
    path('lessons/add/', views.LessonClassListAdd  ,name='LessonClassListAdd'),
    path('lessons/list/', views.LessonClassListList.as_view()  ,name='LessonClassListList'),
    
    
]