from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from apps.student.models import Student,StudentList
from django.conf import settings
from django.views.generic.list import ListView
from ..classes.models import ClassLevels,Classes,ClassNames
from ..home.models import Session,Period
from ..attendance.models import LessonPeriods,DailyAttendance
import datetime
from django.contrib import messages
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
def stdattreportindex(request):
    sessionUpdate(request)
    day =datetime.date.today()
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    lesPeriods=LessonPeriods.objects.all()
    absentStudentList = DailyAttendance.objects.filter(day=day)
    #sessions = Session.objects.all()
    #periods=Period.objects.all()
    
    #studentList = StudentList.objects.all()
    newlist=[]
    
    if request.GET:
        sessionUpdate(request)
        
        session=Session.objects.get(active=True)
        period=Period.objects.get(active=True)
        className = request.GET.get("className")
        classLevel = request.GET.get("classLevel")
        try:
            report_date = request.GET.get("report_date")
            report_date = datetime.datetime.strptime((report_date.replace("-"," ")),"%Y %m %d").date()
        except:
            if report_date == None:
                context = {
                    'sessions':sessions,
                    'periods':periods,
                    'lesPeriods':lesPeriods,
                    'classNames':classNames,
                    'classLevels':classLevels,
                }
                return render(request, "reports/rpr-yoklama.html", context)
            
        if report_date == "" or report_date > day:
            messages.error(request,"Lütfen geçerli bir tarih giriniz")
            context = {
                'sessions':sessions,
                'periods':periods,
                'lesPeriods':lesPeriods,
                'classNames':classNames,
                'classLevels':classLevels,
            }
            return render(request, "reports/rpr-yoklama.html", context)
          
        if className==None or classLevel==None:
            className="A"
            classLevel="9"
        
        studentsList = Student.objects.filter(
            studentlist__className__className__name__contains=className,
            studentlist__className__level__level__contains=classLevel,
            studentlist__session__session__contains=session,
            studentlist__periods__period__contains=period)
            
        for student in studentsList:
            statusList = []
            for x in lesPeriods:
                studentss = DailyAttendance.objects.filter(lesPeriod=x.pk,day=report_date,student=student)
                if studentss:
                    statusList.append("YOK")
                else:
                    statusList.append("VAR")
            newlist.append([student,statusList])
    else:
        
        for listem in StudentList.objects.filter():
            studentList= listem.students.all()
          
           
    context = {
        #'students' : students,
        #'studentList':studentList,
        'sessions':sessions,
        'periods':periods,
        'lesPeriods':lesPeriods,
        'classNames':classNames,
        'classLevels':classLevels,
        'newlist':newlist,
        'media_url':settings.MEDIA_URL,
    }
    return render(request, "reports/rpr-yoklama.html", context)
    
