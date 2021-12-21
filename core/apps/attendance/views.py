from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from apps.student.models import Student,StudentList
from django.conf import settings
from django.views.generic.list import ListView
from ..classes.models import ClassLevels,Classes,ClassNames
from ..home.models import Session,Period
from .models import LessonPeriods,DailyAttendance
import datetime
sessions = Session.objects.all()
periods = Period.objects.all()
# Create your views here.

def sessionUpdate(request):
    if request.GET.get("sessionID"):
        try:
            oldSession = Session.objects.get(active=1)
            oldSession.active=False
            oldSession.save()
        except:
            pass
        newSession=request.GET.get("sessionID")
        print("Yeni sezon : ",newSession)
        newSession = Session.objects.get(session=newSession)
        newSession.active=True
        newSession.save()
    if request.GET.get("periodID"):
        try:
            oldPeriod = Period.objects.get(active=1)
            oldPeriod.active=False
            oldPeriod.save()
        except:
            pass
        newPeriod =request.GET.get("periodID")
        print("Yeni Period  : ",newPeriod )
        newPeriod  = Period.objects.get(period=newPeriod )
        newPeriod.active=True
        newPeriod.save()






@login_required(login_url="/login/")
def stdAttUpdate(request,pk=None):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    try:
        
        student = Student.objects.get(id=pk)
        className = StudentList.objects.get(students=student,session=session,periods=period)
    except:
        context={
        
        'sessions':sessions,"periods":periods
        }
        return render(request,"student/std-list.html",context)
    
    
    context={
        'student':student,
        'className':className,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods
        }
    return render(request, "student/std-Update.html", context)

@login_required(login_url="/login/")
def stdAttView(request,pk=None):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    try:
        student = Student.objects.get(id=pk)
        className = StudentList.objects.get(students=student,session=session,periods=period)
    except:
        context={
        
        'sessions':sessions,"periods":periods
        }
        return render(request,"student/std-list.html",context)
    context={
        'student':student,
        'className':className,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods
        }
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def stdAttShowList(request):
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
def stdAttDelete(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def stdAttIndex(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "attendance/std-dailyAttendance.html", context)


class StdAttDailyListView(ListView):
    template_name = 'attendance/std-dailyAttendance.html'
    model = Student
    

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessonPeriod']=LessonPeriods.objects.all()
        context['classLevels']=ClassLevels.objects.all()
        context['sessions']=Session.objects.all()
        context['periods']=Period.objects.all()
        context['classNames']=ClassNames.objects.all()
        context['media_url'] =settings.MEDIA_URL
        context['dailyattendance']=DailyAttendance.objects.filter(day=datetime.date(year=2021,month=12,day=21))
        
        return context
    def get_queryset(self):
        queryset = {"studentlist": StudentList.objects.filter(className=1)}
        
        sessionUpdate(self.request)
        
        session=Session.objects.get(active=True)
        period=Period.objects.get(active=True)
        className = self.request.GET.get("className")
        classLevel = self.request.GET.get("classLevel")
        attandanceList = self.request.GET.getlist("cb-1")
        day = datetime.date(year=2021,month=12,day=21)
        for item in attandanceList:
            newAttandance = DailyAttendance()
            lessonID,studentID = item.split("-")
            try: 
                DailyAttendance.objects.get(lesPeriod=lessonID,student=studentID,day=day)
               # newAttandance.update(lesPeriod=lessonID,student=studentID,day=day)
                print("kayıt var ?")
                continue
            except:
                    
                newAttandance.lesPeriod=LessonPeriods.objects.get(id=lessonID)
                newAttandance.periods=period
                newAttandance.session=session
                newAttandance.student=Student.objects.get(id=studentID)
                newAttandance.save()
        query={}
        query2={}
        
           
        if className!="0" and className!=None:
            query['studentlist__className__className__name__contains']=className
            query2['className__className__name__contains']=className
        else:
            query['studentlist__className__className__name__contains']=""
            query2['className__className__name__contains']=""
        if classLevel!="0" and classLevel!=None:
            query['studentlist__className__level__level__contains']=classLevel
            query2['className__level__level__contains']=classLevel
        else:
            query['studentlist__className__level__level__contains']=""
            query2['className__level__level__contains']=""
            
        query["studentlist__session__session__contains"]=session
        query["studentlist__periods__period__contains"]=period
        query2["session__session__contains"]=session
        query2["periods__period__contains"]=period
        try:
            queryset = {"students": Student.objects.filter(**query),"studentlist": StudentList.objects.filter(**query2)}  
            
        except:
            print("sorgu hatası")
            

        return queryset


# Create your views here.
