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
        if request.POST:
            
            student.save()
    except:
        context={
        
        'sessions':sessions,"periods":periods
        }
        return render(request,"student/att-list.html",context)
    
    
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
def stdAttDelete(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def stdAttIndex(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "attendance/std-dailyAttendance.html", context)



@login_required(login_url="/login/")
def stdAttShowList(request):
    day =datetime.date.today()
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    lesPeriods=LessonPeriods.objects.filter(session=session,periods=period)
    absentStudentList = DailyAttendance.objects.filter(day=day)
    #sessions = Session.objects.all()
    #periods=Period.objects.all()
    
    #studentList = StudentList.objects.all()
    newlist=[]
    
    
    if request.GET:
        sessionUpdate(request)
        
        className = request.GET.get("className")
        classLevel = request.GET.get("classLevel")
        attandanceList = request.GET.getlist("cb-1")
          
        if className==None or classLevel==None:
            className="A"
            classLevel="9"
        
        studentsList = Student.objects.filter(
            studentlist__className__className__name__contains=className,
            studentlist__className__level__level__contains=classLevel,
            studentlist__session__session__contains=session,
            studentlist__periods__period__contains=period)
        if attandanceList:
            for item in attandanceList:
                newAttandance = DailyAttendance()
                lessonID,studentID,status = item.split("-")
                print(lessonID,studentID,status)
                try: 
                    oldAttandance = DailyAttendance.objects.get(lesPeriod=lessonID,student=studentID,day=day)
                    # newAttandance.update(lesPeriod=lessonID,student=studentID,day=day)
                    
                    if status=="0":
                        oldAttandance.delete()
                    print("kayıt var ?")
                    continue
                except:
                    newAttandance.lesPeriod=LessonPeriods.objects.get(id=lessonID)
                    newAttandance.student=Student.objects.get(id=studentID)
                    newAttandance.periods=period
                    newAttandance.session=session  
                    newAttandance.save()
            
        studentsx=[]

        for x in lesPeriods:
            
            statusList=[]
            for student in studentsList:
                studentss = DailyAttendance.objects.filter(lesPeriod=x.pk,day=day,student=student)
                
                if studentss :
                    
                        
                    statusList.append(True)
                    
                else:
                    statusList.append(False)
           
            studentsx.append(zip(studentsList,statusList))
            
        newlist = zip(lesPeriods,studentsx)
        
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
        'media_url':settings.MEDIA_URL
    }
    
    return render(request, "attendance/std-dailyAttendance.html", context)

@login_required(login_url="/login/")
def lessonPeriodList(request):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    session_id = session.id
    period=Period.objects.get(active=True)
    period_id = period.id
    lesPeriods = LessonPeriods.objects.filter(session_id=session_id,periods_id=period_id)
    if request.GET:
        if request.GET.get("add"):
            if len(lesPeriods) > 0:
                Period_time_list = str(lesPeriods[len(lesPeriods) - 1]).split("-")
                hour_value = int(Period_time_list[2].split(":")[0])
                minute_value = int(Period_time_list[2].split(":")[1])+10
                if minute_value > 59:
                    hour_value += 1
                    minute_value = minute_value - 60
                hour_value_end = hour_value
                minute_value_end = minute_value + 40
                if hour_value == 0:
                    hour_value = "00"
                if minute_value == 0:
                    minute_value = "00"
                if minute_value_end > 59:
                    hour_value_end += 1
                    minute_value_end = minute_value_end - 60
                if hour_value_end == 0:
                    hour_value_end = "00"
                if minute_value_end == 0:
                    minute_value_end = "00"
                id = str(len(lesPeriods)+1)
                #str(hour_value)+":"+str(minute_value)+"-"+str(hour_value_end)+":"+str(minute_value_end)
                new_lesPeriod = LessonPeriods(lessCount=id,periods=period,session=session,lessName = id+".Ders",lesPeriod=str(hour_value)+":"+str(minute_value)+"-"+str(hour_value_end)+":"+str(minute_value_end))
                new_lesPeriod.save()
            else:
                new_lesPeriod = LessonPeriods(lessName = "1.Ders",periods=period,session=session,lessCount="1")
                new_lesPeriod.save()
            return redirect("lesperiod-edit")
        if request.GET.get("delete"):
            id = str(len(lesPeriods))
            old_lesPeriod = LessonPeriods.objects.filter(lessCount=id,periods=period,session=session)
            old_lesPeriod.delete()
            return redirect("lesperiod-edit")
        if request.GET.get("change"):
            for i in range(1,len(lesPeriods)+1):
                i = str(i)
                start = request.GET.get(i+"-start")
                end = request.GET.get(i+"-end")
                start_end = start + "-" + end
                old_lesPeriod_object = LessonPeriods.objects.get(lessCount=i,session_id=session_id,periods_id=period_id)
                old_lesPeriod_object.lesPeriod = start_end
                old_lesPeriod_object.save()
            return redirect("lesperiod-edit")
    lesPeriods=LessonPeriods.objects.filter(session_id=session_id,periods_id=period_id)
    all_lesPeriods = []
    lessonCount = 1

    for i in lesPeriods:
        Period_list = str(i).split("-")
        all_lesPeriods.append([Period_list[0],Period_list[1],Period_list[2],str(lessonCount)])
        lessonCount += 1
        
    context={
        'lesPeriods':all_lesPeriods,
        'sessions':sessions,
        'periods':periods,
        'media_url':settings.MEDIA_URL
    }
    return render(request, "attendance/lessonPeriods.html",context)
# Create your views here.
