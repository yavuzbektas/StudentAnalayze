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
def stdAttDelete(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def stdAttIndex(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "attendance/std-dailyAttendance.html", context)


# class StdAttDailyListView(ListView):
#     template_name = 'attendance/std-dailyAttendance.html'
#     model = Student
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['lessonPeriod']=LessonPeriods.objects.all()
#         context['classLevels']=ClassLevels.objects.all()
#         context['sessions']=Session.objects.all()
#         context['periods']=Period.objects.all()
#         context['classNames']=ClassNames.objects.all()
#         context['newlist']=LessonPeriods.objects.all()
#         context['media_url'] =settings.MEDIA_URL
#         #context['dailyattendance']=DailyAttendance.objects.filter(day=datetime.date(year=2021,month=12,day=23))
        
        
        
#         dalist1 = []
#         dalist2 = []
#         # for i in context["dailyattendance"]:
#         #     if i.student.id not in dalist1:
#         #         dalist1.append(i.student.id)
#         #         i.student.id
#         #     if i.lesPeriod.id not in dalist2:
#         #         dalist2.append(i.lesPeriod.id)
        
#         # context["dalist1"] = dalist1
#         # context["dalist2"] = dalist2
        
#         return context
#     def get_queryset(self):
#         queryset = {"student": StudentList.objects.filter(className=1)}
        
#         sessionUpdate(self.request)
        
#         session=Session.objects.get(active=True)
#         period=Period.objects.get(active=True)
#         className = self.request.GET.get("className")
#         classLevel = self.request.GET.get("classLevel")
#         attandanceList = self.request.GET.getlist("cb-1")
#         day = datetime.date(year=2021,month=12,day=23)
        
        
        
        
        
#         for item in attandanceList:
#             newAttandance = DailyAttendance()
#             lessonID,studentID,status = item.split("-")
#             print(lessonID,studentID,status)
#             try: 
#                 oldAttandance = DailyAttendance.objects.get(lesPeriod=lessonID,student=studentID,day=day)
#                 # newAttandance.update(lesPeriod=lessonID,student=studentID,day=day)
#                 if status=="0":
#                     oldAttandance.delete()
#                 print("kayıt var ?")
#                 continue
#             except:
#                 newAttandance.lesPeriod=LessonPeriods.objects.get(id=lessonID)
#                 newAttandance.student=Student.objects.get(id=studentID)
#                 newAttandance.periods=period
#                 newAttandance.session=session  
#                 newAttandance.save()
#         query={}
#         query2={}
        
           
#         if className!="0" and className!=None:
#             query['studentlist__className__className__name__contains']=className
#             query2['className__className__name__contains']=className
#         else:
#             query['studentlist__className__className__name__contains']="A"
#             query2['className__className__name__contains']=""
#         if classLevel!="0" and classLevel!=None:
#             query['studentlist__className__level__level__contains']=classLevel
#             query2['className__level__level__contains']=classLevel
#         else:
#             query['studentlist__className__level__level__contains']="9"
#             query2['className__level__level__contains']=""
            
#         query["studentlist__session__session__contains"]=session
#         query["studentlist__periods__period__contains"]=period
#         query2["session__session__contains"]=session
#         query2["periods__period__contains"]=period
#         try:
            
#             queryset = {"students": Student.objects.filter(**query),"studentlist": StudentList.objects.filter(**query2)}  
            
#             #queryset = {"students": Student.objects.filter(**query)}
#             day = datetime.date(year=2021,month=12,day=23)
#             studentsList =Student.objects.all()
#             lesPeriods=LessonPeriods.objects.all()
            
#             newlist=[]
#             for x in lesPeriods:
#                 mylist=[]
#                 for student in studentsList:
                    
#                     try:
#                         DailyAttendance.objects.get(lesPeriod=x.pk,student=student.pk,day=day)
                            
#                         student.attStatus = True
                        
#                     except:
#                         student.attStatus = False
                    
#                     mylist.append(student)
#                 x.studentsList=mylist 
#                 newlist.append(x)
#             print(newlist)
#             queryset = {"newlist":newlist}
#         except Exception as err:
#             print(err)
            

#         return queryset

@login_required(login_url="/login/")
def stdAttShowList(request):
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
# Create your views here.
