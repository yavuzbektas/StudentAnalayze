from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Student,StudentList
from django.conf import settings
from .filter import StudentFilter
from django.conf import settings
from django.views.generic.list import ListView
from ..classes.models import ClassLevels,Classes,ClassNames
from ..home.models import Session
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
    sessions = Session.objects.all()
    studentList = StudentList.objects.all()
    className="-"
    classLevel="-"
    selectedLevel=[]
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
        session = request.GET["session"]
        
        classLevel = request.GET["classLevel"]
        getFilterBy = filterNames[category]
        filtertext = '{0}__{1}'.format(getFilterBy, 'startswith')
        # "students__{0}__contains='{1}'".format(getFilterBy, getFilterText)
        # **{'students__{0}__contains'.format(getFilterBy,):getFilterText}
        
        for listem in StudentList.objects.filter(
            className__className__name__contains=className,
            className__level__level__contains=classLevel,
            session__session__contains=session):
            studentList = listem.students.filter(**{filtertext: getFilterText})
            # if Student.objects.filter(**{filtertext: getFilterText}):
        #     students = Student.objects.filter(**{filtertext: getFilterText})
            
            # for student in listem.students.filter(**{filtertext: getFilterText}):
            #     studentList.append(student )
        students = studentList
    else:
        
        for listem in StudentList.objects.filter():
            studentList= listem.students.all()
            selectedLevel = listem.className.className.name
            
    context = {
        'students' : students,
        'studentList':studentList,
        'classLevels':classLevels,
        'sessions':sessions,
        'classNames':classNames,
        'selectedLevel' : selectedLevel,
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




class StudentListView(ListView):
    template_name = 'student/std-list.html'
    model = StudentList
    paginate_by = 4  # if pagination is desired
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filterNames = {
        "Seçim Yap" :"all",
        "Kullancı Adı" : "1",
        "Kullanıcı Soyadı" : "2",
        "TC No" : "3",
        "Cinsiyet" : "4",
    }
        
        context['classLevels']=ClassLevels.objects.all()
        context['sessions']=Session.objects.all()
        context['classNames']=ClassNames.objects.all()
        context['filterNames'] =filterNames
        context['media_url'] =settings.MEDIA_URL
        
        #context['students'] = StudentList.students.objects.all()
        return context
    def get_queryset(self):
        queryset = StudentList.objects.all()
        getFilterText = self.request.GET.get("filterTextVal")
        category = self.request.GET.get("category")
        className = self.request.GET.get("className")
        session = self.request.GET.get("session")
        classLevel = self.request.GET.get("classLevel")
        
        if  category and className and classLevel:
            """ Kullancı Adı" : "1",
                "Kullanıcı Soyadı" : "2",
                "TC No" : "3",
                "Cinsiyet" : "4"""
            if category=="all" and className=="all"  and classLevel=="all"  and session:
                queryset = StudentList.objects.filter(
                session__session__contains=session)
            elif category=="all" and className=="all"  and classLevel!="all"  and session:
                queryset = StudentList.objects.filter(
                className__level__level__contains=classLevel,
                session__session__contains=session)
            elif category=="all" and className!="all"  and classLevel=="all"  and session:
                queryset = StudentList.objects.filter(
                className__className__name__contains=className,
                session__session__contains=session)
            elif category=="all" and className!="all"  and classLevel!="all"  and session:
                queryset = StudentList.objects.filter(
                className__className__name__contains=className,
                className__level__level__contains=classLevel,
                session__session__contains=session)
            elif category!="all" and className!="all"  and classLevel!="all"  and session:
                queryset = StudentList.objects.filter(
                className__className__name__contains=className,
                className__level__level__contains=classLevel,
                session__session__contains=session,
                students__firstName__contains=getFilterText)
            elif category!="all" and className=="all"  and classLevel!="all"  and session:
                queryset = StudentList.objects.filter(
                className__level__level__contains=classLevel,
                session__session__contains=session,
                students__firstName__contains=getFilterText)
            elif category!="all" and className!="all"  and classLevel=="all"  and session:
                queryset = StudentList.objects.filter(
                className__className__name__contains=className,
                session__session__contains=session,
                students__firstName__contains=getFilterText)
            else:
                queryset = StudentList.objects.filter(
                session__session__contains=session)
        return queryset

