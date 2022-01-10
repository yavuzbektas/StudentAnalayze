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
        """query["studentlist__session__session__contains"]=session
        query["studentlist__periods__period__contains"]=period"""
        sessionUpdate(self.request)
    
        session=Session.objects.get(active=True)
        period=Period.objects.get(active=True)
        className = self.request.GET.get("className")
        classLevel = self.request.GET.get("classLevel")
        
        """if className==None:
            className="A"
        if classLevel==None:
            classLevel="9" """
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


def StudentListUpdateView(request,pk):
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    studentList=StudentList.objects.all()
    listo = StudentList.objects.get(id=pk)
    student=Student.objects.all()
    ogrenci5=0
    r=Classes.objects.all()
    i=0
    
    if request.GET:
        
        
        
        className = request.GET.get("className")
        classLevel = request.GET.get("classLevel")
        if className==None or classLevel==None:
            className="A"
            classLevel="9"
        
        
        
        secilen = request.GET.getlist("student_check")
      
        liste=secilen
        session=Session.objects.get(active=True)
        period=Period.objects.get(active=True)
        dizi=[]
        for c in r :
                for a in c.className.name:
                    for b in classLevels:       
                        if a != className and b == classLevel:
                            
                            if c.className.name == className and c.level.level == classLevel:
                                        ekleme=StudentList.objects.get(className=c , session=session)
                                        liste2=listo.students.all()
                                        liste= ekleme
                                        ogrenci4=[]
                                        query={}
                                        query2={}
                                        t=0
                                        z=0
                                        h=0
                                        while i<len(secilen):
                                            deger1=secilen[i]
                                            deger2=int(deger1)
                                            ogrenci=Student.objects.get(id=deger2)
                                            print(ekleme)
                                
                                            
                                            deger1=secilen[i]
                                            deger2=int(deger1)
                                            while t<len(listo.students.all()):
                                                
                                                if liste2[t] == ogrenci:
                                                    copy=ogrenci
                                                    ekleme.students.add(ogrenci)
                                                    ekleme.save()
                                                    liste9=[]
                                                    liste9=list(ekleme.students.all())
                                                    print(liste9)
                                                    while h<len(ekleme.students.all()):
                                                        if  liste9[h]==ogrenci:
                                                                
                                                            listo.students.remove(ogrenci)
                                                            listo.save()
                                                            break
                                                        h=h+1
                                                    listo.save()
                                                    break
                                            
                                            t=t+1
                                            
                                            
                                            listo.save()
                                            ekleme.save()
                                            
                                            z=z+1
                                            listo.save()
                                            ekleme.save()
                                            i=i+1
                                        
                                            break

                        elif a == className and b != classLevel:
                                        
                            if c.className.name == className and c.level.level == classLevel:
                                        ekleme=StudentList.objects.get(className=c , session=session)
                                        liste2=listo.students.all()
                                        liste= ekleme
                                        ogrenci4=[]
                                        query={}
                                        query2={}
                                        t=0
                                        z=0
                                        h=0
                                        while i<len(secilen):
                                            deger1=secilen[i]
                                            deger2=int(deger1)
                                            ogrenci=Student.objects.get(id=deger2)
                                            print(ekleme)
                                
                                            
                                            deger1=secilen[i]
                                            deger2=int(deger1)
                                            while t<len(listo.students.all()):
                                                
                                                if liste2[t] == ogrenci:
                                                    copy=ogrenci
                                                    ekleme.students.add(ogrenci)
                                                    ekleme.save()
                                                    liste9=[]
                                                    liste9=list(ekleme.students.all())
                                                    print(liste9)
                                                    while h<len(ekleme.students.all()):
                                                        if  liste9[h]==ogrenci:
                                                                
                                                            listo.students.remove(ogrenci)
                                                            listo.save()
                                                            break
                                                        h=h+1
                                                    listo.save()
                                                    break
                                            
                                            t=t+1
                                            
                                            
                                            listo.save()
                                            ekleme.save()
                                            
                                            z=z+1
                                            listo.save()
                                            ekleme.save()
                                            i=i+1
                                        
                                            break
                        elif a != className and b != classLevel:
                                    
                            if c.className.name == className and c.level.level == classLevel:
                                        ekleme=StudentList.objects.get(className=c , session=session)
                                        liste2=listo.students.all()
                                        liste= ekleme
                                        ogrenci4=[]
                                        query={}
                                        query2={}
                                        t=0
                                        z=0
                                        h=0
                                        while i<len(secilen):
                                            deger1=secilen[i]
                                            deger2=int(deger1)
                                            ogrenci=Student.objects.get(id=deger2)
                                            print(ekleme)
                                
                                            
                                            deger1=secilen[i]
                                            deger2=int(deger1)
                                            while t<len(listo.students.all()):
                                                
                                                if liste2[t] == ogrenci:
                                                    copy=ogrenci
                                                    ekleme.students.add(ogrenci)
                                                    ekleme.save()
                                                    liste9=[]
                                                    liste9=list(ekleme.students.all())
                                                    print(liste9)
                                                    while h<len(ekleme.students.all()):
                                                        if  liste9[h]==ogrenci:
                                                                
                                                            listo.students.remove(ogrenci)
                                                            listo.save()
                                                            break
                                                        h=h+1
                                                    listo.save()
                                                    break
                                            
                                            t=t+1
                                            
                                            
                                            listo.save()
                                            ekleme.save()
                                            
                                            z=z+1
                                            listo.save()
                                            ekleme.save()
                                            i=i+1
                                        
                                            break
                           
        
        
    context = {
        #'students' : students,
        'studentList':listo,
        'sessions':sessions,
        'periods':periods,
        #'studentt':listo,
        'classNames':classNames,
        'classLevels':classLevels,
    
        'media_url':settings.MEDIA_URL
    }
    
    return render(request, "student/studentListUpdate.html", context)