from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Student
from django.conf import settings
from .filter import StudentFilter
from django.conf import settings
from django.views.generic.list import ListView

# Create your views here.
@login_required(login_url="/login/")
def studentUpdate(request):
    context={}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentView(request):
    context={}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentShowList(request):
    students = Student.objects.all()
    
    context = {
        'students' : students,
        #'filterKeys':filterKeys,
        'media_url':settings.MEDIA_URL
    }
    
    return render(request, "student/std-list.html", context)

@login_required(login_url="/login/")
def studentDelete(request):
    context={}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentIndex(request):
    context={}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentShowListFiltered(request,filterBy,filterValue):
    
    
    #...is there some way, given:
    filtertext = '{0}__{1}'.format(filterBy, 'startswith')
    #filterKeys = StudentFilter()
    
    #...that you can run the equivalent of this ?
    
    students = Student.objects.filter(**{filtertext: filterValue})
    context = {
        'students' : students,
        #'filter': filter,
        #'filterKeys':filterKeys,
        'media_url':settings.MEDIA_URL
    }
    return render(request, "student/std-list.html", context)

from django_tables2 import SingleTableView
from .tables import StudentTable


class StudentFilterView(SingleTableView):
    model = Student
    table_class = StudentTable
    template_name = 'student/std-list.html'

# class StudentFilterView(ListView):
#     paginate_by = 3
#     model = Student
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter']=StudentFilter(self.request.GET,queryset=self.get_queryset())
        
#         return context
    
#     template_name="student/std-list.html"
#     def get_queryset(self):
#         queryset = Student.objects.all()
#         if self.request.GET.get("browse"):
#             selection =  Student.objects.all()
#             if selection == "firstname":
#                 queryset = Student.objects.all()
#             elif selection == "lastname":
#                 queryset = Student.objects.all()
#             elif selection == "TC":
#                 queryset = Student.objects.all()
#             else:
#                 queryset = Student.objects.all()
#         return queryset
