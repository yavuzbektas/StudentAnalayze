from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Student,StudentList
from django.conf import settings
from .filter import StudentFilter
from django.conf import settings
from django.views.generic.list import ListView
from ..classes.models import ClassLevels,Classes,ClassNames
from ..home.models import Session,Period
from django.views.generic.detail import SingleObjectMixin
sessions = Session.objects.all()
periods = Period.objects.all()
# Create your views here.
@login_required(login_url="/login/")
def studentUpdate(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentView(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentShowList(request):
    students = Student.objects.all()
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    sessions = Session.objects.all()
    periods=Period.objects.all()
    studentList = StudentList.objects.all()
    className="-"
    classLevel="-"
    selectedLevel=[]
    filterNames = {
        "Kullancı Adı" : "firstName",
        "Kullanıcı Soyadı" : "lastName",
        "TC No" : "TC",
        "Cinsiyet" : "gender",
        "Periyot" : "periods",
    }
    
    if request.GET:
        getFilterText = request.GET["filterTextVal"]
        category = request.GET["category"]
        className = request.GET["className"]
        session = request.GET["session"]
        period = request.GET["period"]
        classLevel = request.GET["classLevel"]
        getFilterBy = filterNames[category]
        filtertext = '{0}__{1}'.format(getFilterBy, 'startswith')
        # "students__{0}__contains='{1}'".format(getFilterBy, getFilterText)
        # **{'students__{0}__contains'.format(getFilterBy,):getFilterText}
        
        for listem in StudentList.objects.filter(
            className__className__name__contains=className,
            className__level__level__contains=classLevel,
            session__session__contains=session,
            period__period__contains=period):
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
        'periods':periods,
        'classNames':classNames,
        'selectedLevel' : selectedLevel,
        'filterNames' :filterNames.keys(),
        'media_url':settings.MEDIA_URL
    }
    
    return render(request, "student/std-list.html", context)

@login_required(login_url="/login/")
def studentDelete(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentIndex(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "student/std-profile.html", context)




class StudentListView(ListView):
    template_name = 'student/std-list.html'
    model = Student

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filterNames = {
        "Seçim Yap" :"0",
        "Kullancı Adı" : "1",
        "Kullanıcı Soyadı" : "2",
        "TC No" : "3",
        "Cinsiyet" : "4",
    }
        
        context['classLevels']=ClassLevels.objects.all()
        context['sessions']=Session.objects.all()
        context['periods']=Period.objects.all()
        context['classNames']=ClassNames.objects.all()
        context['filterNames'] =filterNames
        context['media_url'] =settings.MEDIA_URL
        
        #context['students'] = StudentList.students.objects.all()
        return context
    def get_queryset(self):
        queryset = {"students": Student.objects.all()}
        getFilterText = self.request.GET.get("filterTextVal")
        category = self.request.GET.get("category")
        className = self.request.GET.get("className")
        session = self.request.GET.get("session")
        period = self.request.GET.get("period")
        classLevel = self.request.GET.get("classLevel")
        query={}
        if  className and classLevel:
            """Seçim Yap" :"0",
            "Kullancı Adı" : "1",
            "Kullanıcı Soyadı" : "2",
            "TC No" : "3",
            "Cinsiyet" : "4"""
            
            
            if className!="0":
                query['studentlist__className__className__name__contains']=className
            else:
                query['studentlist__className__className__name__contains']=""
            if classLevel!="0":
                query['studentlist__className__level__level__contains']=classLevel
            #query["studentlist__session__session__contains"]=session
            try:
                queryset = {"students": Student.objects.filter(**query).distinct()}  
                
            except:
                print("sorgu hatası")
            
        print(query,queryset)
        return queryset

