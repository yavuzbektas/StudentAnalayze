from django.shortcuts import render
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
    template_name="student/std-listcopy.html"
    
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
        
        z=0
        i=0  
        liste =[]
        liste=StudentList.objects.all()
        liste2=[]
        liste3=[]
        
        while i<len(StudentList.objects.all()):
                deger=liste[i]
            
                print(session.session)
                print(className)
                if deger.session.session==session.session :
                   
                    
                    queryset = { "studentlist":liste2 }  
                    if deger.className.className.name==className and deger.className.level.level==classLevel:
                        print("a")
               
                        liste2.append(deger) 
                        queryset = { "studentlist":liste2 }
                    elif className==0  and classLevel!=0:
                        if deger.className.level.level==classLevel:
                            liste2.append(deger) 
                            queryset = { "studentlist":liste2 }
                            break
                    elif className==0  and classLevel==0:
                        liste2.append(deger) 
                        queryset = { "studentlist":liste2 }
                    elif className!=0  and classLevel==0:
                        if deger.className.className.name==className:
                            liste2.append(deger) 
                            queryset = { "studentlist":liste2 }
                    elif  className==None  and classLevel==None:
                        print("z")  
                        liste2.append(deger) 
                        queryset = { "studentlist":liste2 }
                     
                    
               
                i=i+1
        return queryset

@login_required(login_url="/login/")
def StudentListUpdateView(request,pk):
    
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    baseList = StudentList.objects.get(id=pk) # get studentlist by current ID
    classess=Classes.objects.all()
    studentIndex=0
    
    if request.GET:
        try:
            session=Session.objects.get(active=True)
            period=Period.objects.get(active=True) 
        except:
            return
        className = request.GET.get("className")
        classLevel = request.GET.get("classLevel")
        if className==None or classLevel==None:
            return 
        chekcedStudentList = request.GET.getlist("student_check")
        #print(chekcedStudentList)
        targetClass =  Classes.objects.get(className=ClassNames.objects.get(name=className),level=ClassLevels.objects.get(level=classLevel))
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
    
    return render(request, "student/studentListUpdate.html", context)