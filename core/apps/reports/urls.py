from django.urls import path, re_path
from apps.reports import views
def repath_func(request):
    from django.http import HttpResponseRedirect


    return HttpResponseRedirect(request.path_info)
urlpatterns = [

    # The home page
    path('attendanceReport/', views.stdattreportindex, name='attreport'),
    
    
    
    
]