from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student
from django.conf import settings

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
    

 #...that you can run the equivalent of this ?
    
    students = Student.objects.filter(**{filtertext: filterValue})
    context = {
        'students' : students,
        'media_url':settings.MEDIA_URL
    }
    return render(request, "student/std-list.html", context)