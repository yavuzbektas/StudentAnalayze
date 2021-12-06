from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Student,StudentList
from django.conf import settings
from .filter import StudentFilter
from django.conf import settings
from django.views.generic.list import ListView
from ..classes.models import ClassLevels,Classes,ClassNames
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
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    
    
    
    filterNames = {
        "Kullancı Adı" : "firstName",
        "Kullanıcı Soyadı" : "lastName",
        "TC No" : "TC",
        "Cinsiyet" : "gender",
    }
    
    if request.GET:
        getFilterText = request.GET["filterTextVal"]
        category = request.GET["category"]
        className = request.GET["className"]
        print(className)
        classLevel = request.GET["classLevel"]
        getFilterBy = filterNames[category]
        # "students__{0}__contains='{1}'".format(getFilterBy, getFilterText)
        # **{'students__{0}__contains'.format(getFilterBy,):getFilterText}
        studentList = []
        for listem in StudentList.objects.filter(
            className__className__name__contains=className,
            className__level__level__contains=classLevel,):
            for student in listem.students.all():
                studentList.append(student )
    
        print(studentList)
        students = studentList
            #...is there some way, given:
        filtertext = '{0}__{1}'.format(getFilterBy, 'startswith')
        #filterKeys = StudentFilter()
        
        #...that you can run the equivalent of this ?
        
        # if Student.objects.filter(**{filtertext: getFilterText}):
        #     students = Student.objects.filter(**{filtertext: getFilterText})
       
    context = {
        'students' : students,
        'studentList':studentList,
        'classLevels':classLevels,
        'classNames':classNames,
        'filterNames' :filterNames.keys(),
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



