from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..student.models import Student
from django.conf import settings

# Create your views here.
@login_required(login_url="/login/")
def classesUpdate(request):
    context={}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesView(request):
    context={}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesShowList(request):
    context={}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesDelete(request):
   context={}
   return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesIndex(request):
    context={}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesShowListFiltered(request,filterBy,filterValue):
    context={}
    return render(request, "classes/cls-9sinif.html", context)


