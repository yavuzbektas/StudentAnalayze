from django.urls import path
from apps.lessons import views
def repath_func(request):
    from django.http import HttpResponseRedirect


    return HttpResponseRedirect(request.path_info)
urlpatterns = [

    
    
    
    
   

    
    
]