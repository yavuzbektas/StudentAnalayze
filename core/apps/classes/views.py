from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from apps.student.views import sessionUpdate
from ..student.models import Student
from django.conf import settings
from ..home.models import Session,Period
from django.views.generic import ListView
from ..student.models import StudentList
from apps.classes.models import ClassLevels, ClassNames, Classes
sessions = Session.objects.all()
periods = Period.objects.all()
# Create your views here.
@login_required(login_url="/login/")
def classesUpdate(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesView(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesShowList(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesDelete(request):
   context={'sessions':sessions,"periods":periods}
   return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesIndex(request):
    context={'sessions':sessions,"periods":periods}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesShowListFiltered(request,filterBy,filterValue):
    context={'sessions':sessions,"periods":periods}
    return render(request, "classes/cls-9sinif.html", context)

class StudentListDetailView(ListView):
    
    model = StudentList
    template_name="clasess/cls-list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['classLevels']=ClassLevels.objects.all()
        context['sessions']=Session.objects.all()
        context['periods']=Period.objects.all()
        context['classNames']=ClassNames.objects.all()
        context['studentlist']=StudentList.objects.all()
        
        return context
    def get_queryset(self):
        queryset = {"studentlist": StudentList.objects.all()}
        sessionUpdate(self.request)
    
        session=Session.objects.get(active=True)
        period=Period.objects.get(active=True)
        className = self.request.GET.get("className")
        classLevel = self.request.GET.get("classLevel")
        query={}
        
           
        if className!="0" and className!=None:
            query['className__className__name__contains']=className
            
        else:
            query['className__className__name__contains']=""
           
        if classLevel!="0" and classLevel!=None:
            query['className__level__level__contains']=classLevel
          
        else:
            query['className__level__level__contains']=""
            
            
        query["session__session__contains"]=session
        query["periods__period__contains"]=period
        try:
            queryset = {"studentlist": StudentList.objects.filter(**query)}  
            
        except:
            print("sorgu hatası") 
        return queryset
        

@login_required(login_url="/login/")
def StudentListUpdateView(request,pk):
    
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    baseList = StudentList.objects.get(id=pk) # get studentlist by current ID
    classess=Classes.objects.all()
    
    
    if request.GET:
        className = request.GET.get("className")
        classLevel = request.GET.get("classLevel")
        chekcedStudentList = request.GET.getlist("student_check")
        
        try:
            session=Session.objects.get(active=True)
            period=Period.objects.get(active=True) 
            targetClass =  Classes.objects.get(className=ClassNames.objects.get(name=className),level=ClassLevels.objects.get(level=classLevel))
        except Exception as err:
            print(err)
            return redirect("/classes/assign")
        
        
       
        if targetClass!=None:
            targetStudentList=StudentList.objects.get(className=targetClass , session=session,periods=period)
       
        for studentID in chekcedStudentList:
            
            targetStudentList.students.add(Student.objects.get(id=int(studentID)))
            baseList.students.remove(Student.objects.get(id=int(studentID)))
            baseList.save()
            targetStudentList.save()
            
                
                                                
    context = {
        
        'studentList':baseList,
        'sessions':sessions,
        'periods':periods,
        'classNames':classNames,
        'classLevels':classLevels,
        'media_url':settings.MEDIA_URL
    }
    
    return render(request, "clasess/cls-listUpdate.html", context)