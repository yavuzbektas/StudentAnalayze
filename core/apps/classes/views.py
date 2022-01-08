from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
    template_name="clasess/std-listcopy.html"
    context_object_name = 'studentlist'


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
        sessionUpdate(request)
        
        
        className = request.GET.get("className")
        classLevel = request.GET.get("classLevel")
        if className==None or classLevel==None:
            className="A"
            classLevel="9"
        
        
        
        
        secilen = request.GET.getlist("student_check")
        print(secilen)
        liste=secilen
        
        dizi=[]
        for c in r :
                for a in c.className.name:
                    for b in classLevels:       
                        if a != className and b == classLevel:
                            
                            if c.className.name == className and c.level.level == classLevel:
                                ekleme=StudentList.objects.get(className=c)
                                liste2=listo.students.all()
                                t=0
                                while i <= len(liste)-1:
                                    deger1=secilen[i]
                                    deger2=int(deger1)
                                    while t<=len(listo.students.all())-1:
                                        ogrenci=Student.objects.get(id=deger2)
                                        if liste2[t] == ogrenci:
                                            
                                            ekleme.students.add(ogrenci)
                                            listo.save()
                                            ekleme.save()
                                            """listo.delete(ogrenci)"""
                                            break
                                        t=t+1
                                    
                                    
                                    listo.save()
                                    ekleme.save()
                                    
                                    i=i+1
                                listo.save()
                                ekleme.save()
                                    
                                
                                break

                        elif a == className and b != classLevel:
                                        
                            if c.className.name == className and c.level.level == classLevel:
                                ekleme=StudentList.objects.get(className=c)
                                liste2=listo.students.all()
                                ogrenci4=[]
                                t=0
                                z=0
                                while i < len(liste):
                                    deger1=secilen[i]
                                    deger2=int(deger1)
                                    while t<len(listo.students.all()):
                                        ogrenci=Student.objects.get(id=deger2)
                                        if liste2[t] == ogrenci:
                                           
                                            ekleme.students.add(ogrenci)
                                            ekleme.save()
                                            
                                            """if listo.students.all() != ogrenci:
                                                listo.students.set(listo.students.get(id=ogrenci.id))
                                                listo.save()"""
                                            listo.save()
                                            break
                                    
                                        t=t+1
                                    
                                    
                                    listo.save()
                                    ekleme.save()
                                    
                                    i=i+1
                                listo.save()
                                ekleme.save()
                                    
                                
                                break
                        elif a != className and b != classLevel:
                                    
                            if c.className.name == className and c.level.level == classLevel:
                                
                                ekleme=StudentList.objects.get(className=c)
                                liste2=listo.students.all()
                                
                                
                                t=0
                                while i < len(liste):
                                    deger1=secilen[i]
                                    deger2=int(deger1)
                                    while t<len(listo.students.all()):
                                        ogrenci=Student.objects.get(id=deger2)
                                        if liste2[t] == ogrenci:
                                            
                                            ekleme.students.add(ogrenci)
                                
                                            ekleme.save()
                                            """listo.delete(ogrenci)"""
                                            listo.save()
                                            break
                                        t=t+1
                                    
                                    

                                    listo.save()
                                    ekleme.save()
                                    
                                    i=i+1
                                listo.save()
                                ekleme.save()
                                    
                                
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