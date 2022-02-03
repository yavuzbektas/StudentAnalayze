import numbers
from operator import le
from os import name
from django.forms import BaseInlineFormSet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from apps.student.views import sessionUpdate
from apps.student.models import Student
from django.conf import settings
from apps.home.models import Session,Period
from django.views.generic import ListView
from apps.student.models import StudentList
from apps.classes.form import ClassListForm
from apps.classes.models import ClassLevels, ClassNames, Classes
from apps.classes.classes_for_sidebar import all_class_levels
sessions = Session.objects.all()
periods = Period.objects.all()
classes = Classes.objects.all()

all_class_levels = all_class_levels()

# Create your views here.
def success(request):
    studentList=StudentList.objects.all()
    student=Student.objects.all()
    clasess=Classes.objects.all()
    sinnif9=ClassLevels.objects.filter(level="9")
    sinnif10=ClassLevels.objects.filter(level="10")
    sinnif11=ClassLevels.objects.filter(level="11")
    sinnif12=ClassLevels.objects.filter(level="12")
    class9=Classes.objects.filter(level=sinnif9[0])
    class10=Classes.objects.filter(level=sinnif10[0])
    class11=Classes.objects.filter(level=sinnif11[0])
    class12=Classes.objects.filter(level=sinnif12[0])
    classlistx9=StudentList.objects.filter(className__in=class9)
    classlistx10=StudentList.objects.filter(className__in=class10)
    classlistx11=StudentList.objects.filter(className__in=class11)
    classlistx12=StudentList.objects.filter(className__in=class12)
   
    context = {'segment': 'index','sessions':sessions,"periods":periods,'all_class_levels':all_class_levels,'studentList':studentList,"student":student,"clasess":clasess,"class9":classlistx9,"class10":classlistx10,"class11":classlistx11,"class12":classlistx12}

    return render(request, "clasess/cls-Success.html", context)
@login_required(login_url="/login/")
def classesAdd(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesUpdate(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesView(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesShowList(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesDelete(request,pk):
    baseList = StudentList.objects.get(id=pk)
    baseList.delete()
    classes = Classes.objects.all()
    all_class_levels = []
    all_class_levels_levels = []
    for i in classes:
        if i.level not in all_class_levels:
            all_class_levels.append(i.level)

    for i in all_class_levels:
        names = []
        for x in classes:
            if x.level == i:
                names.append(x.className)
        for z in names:
            names[names.index(z)] = str(names[names.index(z)])
        names.sort()
        all_class_levels[all_class_levels.index(i)] = (str(all_class_levels[all_class_levels.index(i)]),names)

    for i in all_class_levels:
        all_class_levels_levels.append(int(i[0]))
    all_class_levels_levels.sort()
    for i in all_class_levels_levels:
        all_class_levels_levels[all_class_levels_levels.index(i)] = str(all_class_levels_levels[all_class_levels_levels.index(i)])

    for i in all_class_levels_levels:
        for x in all_class_levels:
            if i == x[0]:
                all_class_levels_levels[all_class_levels_levels.index(i)] = (all_class_levels_levels[all_class_levels_levels.index(i)],x[1])
    for i in all_class_levels_levels:
        for name in i[1]:
            name_count=i[1].count(name)
            if name_count > 1:
                for count in range(name_count-1):
                    i[1].remove(name)
    classes_all = []
    for i in StudentList.objects.all():
        if str(i.className) not in classes_all:
            classes_all.append(str(i.className))
    for i in all_class_levels_levels:
        for name in i[1]:
            if i[0]+name not in classes_all:
                all_class_levels_levels[all_class_levels_levels.index(i)][1].remove(name)
        if i[1] == []:
            all_class_levels_levels.remove(i)
    all_class_levels = all_class_levels_levels
    return redirect("classes")

@login_required(login_url="/login/")
def classesIndex(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "classes/cls-9sinif.html", context)

@login_required(login_url="/login/")
def classesShowListFiltered(request,filterBy,filterValue):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
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
        
        
        # if baseList.className != targetClass.className 
        print(chekcedStudentList)
        if targetClass!=None:
            targetStudentList=StudentList.objects.get(className=targetClass , session=session,periods=period)

        print(targetStudentList)
        if baseList.className != targetStudentList.className:
            for studentID in chekcedStudentList:
                print(chekcedStudentList)
                targetStudentList.students.add(Student.objects.get(id=studentID))
                baseList.students.remove(Student.objects.get(id=studentID))
                baseList.save()
                targetStudentList.save()

                
        return redirect('/classes/assign/')                                        
    context = {
        
        'studentList':baseList,
        'sessions':sessions,
        'periods':periods,
        'classNames':classNames,
        'classLevels':classLevels,
        'media_url':settings.MEDIA_URL,
        'all_class_levels':all_class_levels
    }
    
    return render(request, "clasess/cls-listUpdate.html", context)

@login_required(login_url="/login/")
def classesListIndex(request):
    sessionUpdate(request)
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    newclassform = ClassListForm()
    classList = StudentList.objects.filter(session=session,periods=period)
    
    if request.POST:
        if request.POST.get("cnnewvaluesave"):
            newname = request.POST.get("cnnewvalue")
            tnn = len(str(newname))
            if tnn != 1:
                return redirect("classes")
            try:
                tnn = int(newname)
                return redirect("classes")
            except:
                newname = str(newname).upper()
                oldnameobjects = ClassNames.objects.filter(name = newname)
                if oldnameobjects:
                    return redirect("classes")
                newnameobject = ClassNames(name=newname)
                newnameobject.save()
        if request.POST.get("cnvaluesave"):
            name_id = request.POST.get("classnameadd")
            if name_id == "":
                newname = request.POST.get("cnvalue")
                tnn = len(str(newname))
                if tnn != 1:
                    return redirect("classes")
                try:
                    tnn = int(newname)
                    return redirect("classes")
                except:
                    newname = str(newname).upper()
                    oldnameobjects = ClassNames.objects.filter(name = newname)
                    if oldnameobjects:
                        return redirect("classes")
                    newnameobject = ClassNames(name=newname)
                    newnameobject.save()
                    
            else:
                try:
                    name = ClassNames.objects.filter(id=name_id)[0]
                except:
                    return redirect("classes")
                newname = request.POST.get("cnvalue")
                if newname == "":
                    newnameobject = ClassNames.objects.get(id=name_id)
                    newnameobject.delete()
                else:
                    tnn = len(str(newname))
                    if tnn != 1:
                        return redirect("classes")
                    try:
                        tnn = int(newname)
                    except:
                        newname = str(newname).upper
                        newnameobject = ClassNames.objects.get(id=name_id)
                        newnameobject.name = newname
                        newnameobject.save()
        if request.POST.get("clvaluenewsave"):
            newlevel = request.POST.get("clvaluenew")
            try:
                tnl = int(newlevel)
            except:
                return redirect("classes")
            oldlevelobjects = ClassLevels.objects.filter(level = newlevel)
            if oldlevelobjects:
                return redirect("classes")
            newlevelobject = ClassLevels(level=newlevel)
            newlevelobject.save()
        if request.POST.get("clvaluesave"):
            level_id = request.POST.get("classesidadd")
            if level_id == "":
                newlevel = request.POST.get("clvalue")
                try:
                    tnl = int(newlevel)
                except:
                    return redirect("classes")
                oldlevelobjects = ClassLevels.objects.filter(level = newlevel)
                if oldlevelobjects:
                    return redirect("classes")
                newlevelobject = ClassLevels(level=newlevel)
                newlevelobject.save()
            else:
                try:
                    level = ClassLevels.objects.filter(id=level_id)[0]
                except:
                    return redirect("classes")
                newlevel = request.POST.get("clvalue")
                if newlevel == "":
                    newlevelobject = ClassLevels.objects.get(id=level_id)
                    newlevelobject.delete()
                else:
                    try:
                        tnl = int(newlevel)
                    except:
                        return redirect("classes")
                    newlevelobject = ClassLevels.objects.get(id=level_id)
                    newlevelobject.level = newlevel
                    newlevelobject.save()
            
        if request.POST.get("_addanother"):
            level = request.POST.get("classesidadd")
            name = request.POST.get("classnameadd")
            if level != "" and name != "":
                try:
                    level = ClassLevels.objects.filter(id=level)[0]
                    name = ClassNames.objects.filter(id=name)[0]
                except:
                    return redirect("classes")
                newclass = Classes(className=name,level=level)
                if Classes.objects.filter(className=name,level=level):
                    for i in StudentList.objects.all():
                        if(str(i.className) == str(newclass)) and str(i.periods) == str(period):
                            classes = Classes.objects.all()
                            all_class_levels = []
                            all_class_levels_levels = []
                            for i in classes:
                                if i.level not in all_class_levels:
                                    all_class_levels.append(i.level)

                            for i in all_class_levels:
                                names = []
                                for x in classes:
                                    if x.level == i:
                                        names.append(x.className)
                                for z in names:
                                    names[names.index(z)] = str(names[names.index(z)])
                                names.sort()
                                all_class_levels[all_class_levels.index(i)] = (str(all_class_levels[all_class_levels.index(i)]),names)

                            for i in all_class_levels:
                                all_class_levels_levels.append(int(i[0]))
                            all_class_levels_levels.sort()
                            for i in all_class_levels_levels:
                                all_class_levels_levels[all_class_levels_levels.index(i)] = str(all_class_levels_levels[all_class_levels_levels.index(i)])

                            for i in all_class_levels_levels:
                                for x in all_class_levels:
                                    if i == x[0]:
                                        all_class_levels_levels[all_class_levels_levels.index(i)] = (all_class_levels_levels[all_class_levels_levels.index(i)],x[1])
                            for i in all_class_levels_levels:
                                for name in i[1]:
                                    name_count=i[1].count(name)
                                    if name_count > 1:
                                        for count in range(name_count-1):
                                            i[1].remove(name)
                            classes_all = []
                            for i in StudentList.objects.all():
                                if str(i.className) not in classes_all:
                                    classes_all.append(str(i.className))
                            for i in all_class_levels_levels:
                                for name in i[1]:
                                    if i[0]+name not in classes_all:
                                        all_class_levels_levels[all_class_levels_levels.index(i)][1].remove(name)
                                if i[1] == []:
                                    all_class_levels_levels.remove(i)
                            all_class_levels = all_class_levels_levels
                            context={
                                'sessions':sessions,
                                'periods':periods,
                                'classNames':classNames,
                                'classLevels':classLevels,
                                'classList':classList,
                                'newclassform':newclassform,
                                'error':True,
                                'all_class_levels':all_class_levels
                                }
                            return render(request, "clasess/cls-add.html", context)
                if Classes.objects.filter(className=name,level=level):
                    newclass = (Classes.objects.filter(className=name,level=level))[0]
                else:
                    newclass.save()
                newclassList = StudentList(session=session,periods=period,className=newclass)
                newclassList.save()
    classList = StudentList.objects.filter(session=session,periods=period)
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    classes = Classes.objects.all()
    all_class_levels = []
    all_class_levels_levels = []
    for i in classes:
        if i.level not in all_class_levels:
            all_class_levels.append(i.level)

    for i in all_class_levels:
        names = []
        for x in classes:
            if x.level == i:
                names.append(x.className)
        for z in names:
            names[names.index(z)] = str(names[names.index(z)])
        names.sort()
        all_class_levels[all_class_levels.index(i)] = (str(all_class_levels[all_class_levels.index(i)]),names)

    for i in all_class_levels:
        all_class_levels_levels.append(int(i[0]))
    all_class_levels_levels.sort()
    for i in all_class_levels_levels:
        all_class_levels_levels[all_class_levels_levels.index(i)] = str(all_class_levels_levels[all_class_levels_levels.index(i)])

    for i in all_class_levels_levels:
        for x in all_class_levels:
            if i == x[0]:
                all_class_levels_levels[all_class_levels_levels.index(i)] = (all_class_levels_levels[all_class_levels_levels.index(i)],x[1])
    for i in all_class_levels_levels:
        for name in i[1]:
            name_count=i[1].count(name)
            if name_count > 1:
                for count in range(name_count-1):
                    i[1].remove(name)
    classes_all = []
    for i in StudentList.objects.all():
        if str(i.className) not in classes_all:
            classes_all.append(str(i.className))
    for i in all_class_levels_levels:
        for name in i[1]:
            if i[0]+name not in classes_all:
                all_class_levels_levels[all_class_levels_levels.index(i)][1].remove(name)
        if i[1] == []:
            all_class_levels_levels.remove(i)
    all_class_levels = all_class_levels_levels
    
    context={
        'sessions':sessions,
        'periods':periods,
        'classNames':classNames,
        'classLevels':classLevels,
        'classList':classList,
        'newclassform':newclassform,
        'error':False,
        'all_class_levels':all_class_levels
        }
    return render(request, "clasess/cls-add.html", context)

@login_required(login_url="/login/")
def classesListUpdate(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "clasess/cls-add.html", context)

@login_required(login_url="/login/")
def classesListDelete(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "clasess/cls-add.html", context)

@login_required(login_url="/login/")
def classesListView(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "clasess/cls-add.html", context)

def classesListAdd(request,classlevelID,classnameID):
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    
    newclassform =ClassListForm()
    if newclassform.is_valid():
        
        newclassform.className.id=classnameID
        newclassform.classLevel.id=classlevelID
        newclassform.session.id=session.id
        newclassform.periods.id=period.id
        newclassform.save()
    
    context={
        'sessions':sessions,
        "periods":periods,
        'all_class_levels':all_class_levels,
        
        }
    return render(request, "clasess/cls-add.html", context)

@login_required(login_url="/login/")
def UpdateSeating(request,pk):
    classNames = ClassNames.objects.all()
    classLevels = ClassLevels.objects.all()
    baseList = StudentList.objects.get(id=pk)
    if request.POST:
        c1r1 = request.POST.get("c1r1")
        c1r2 = request.POST.get("c1r2")
        c2r1 = request.POST.get("c2r1")
        c2r2 = request.POST.get("c2r2")
        c3r1 = request.POST.get("c3r1")
        c3r2 = request.POST.get("c3r2")
        c4r1 = request.POST.get("c4r1")
        c4r2 = request.POST.get("c4r2")
        c1r11 = request.POST.get("c1r11")
        c1r21 = request.POST.get("c1r21")
        c2r11 = request.POST.get("c2r11")
        c2r21 = request.POST.get("c2r21")
        c3r11 = request.POST.get("c3r11")
        c3r21 = request.POST.get("c3r21")
        c4r11 = request.POST.get("c4r11")
        c4r21 = request.POST.get("c4r21")
        c1r12 = request.POST.get("c1r12")
        c1r22 = request.POST.get("c1r22")
        c2r12 = request.POST.get("c2r12")
        c2r22 = request.POST.get("c2r22")
        c3r12 = request.POST.get("c3r12")
        c3r22 = request.POST.get("c3r22")
        c4r12 = request.POST.get("c4r12")
        c4r22 = request.POST.get("c4r22")
        try:
            arrangement = (c1r1+"/"+c1r2+"/"+c2r1+"/"+c2r2+"/"+c3r1+"/"+c3r2+"/"+c4r1+"/"+c4r2+"/"+c1r11+"/"+c1r21+"/"+c2r11+"/"+c2r21+"/"+c3r11+"/"+c3r21+"/"+c4r11+"/"+c4r21+"/"+c1r12+"/"+c1r22+"/"+c2r12+"/"+c2r22+"/"+c3r12+"/"+c3r22+"/"+c4r12+"/"+c4r22)
            baseList.seating_arrangement = arrangement
            baseList.save()
            baseList = StudentList.objects.get(id=pk)
        except:
            pass
        return HttpResponseRedirect(str(pk))
    arrangement = baseList.seating_arrangement
    students = arrangement.split("/")
    students_all = list(baseList.students.all())
    students_sitting = []
    student_ids = []
    student_names = []
    student_genders = []
    for i in students:
        if i != " ":
            students_sitting.append(i)
    for student in baseList.students.all():
        student_ids.append(str(student.id))
        student_names.append(student.firstName+" "+student.lastName)
    students_not_sitting = list(zip(student_ids,student_names))
    try:
        if(students_not_sitting[1][0] in students_sitting):
            students_not_sitting.remove(students_not_sitting[1])
    except:
        pass
    for student in students_not_sitting:
        if student[0] in students_sitting:
            students_not_sitting.remove(student)

    if len(student_ids) == len(students_sitting):
        students_not_sitting = []

    if students_not_sitting != []:
        for student in students_not_sitting:
            student_object = Student.objects.get(id=student[0])
            try:
                students_not_sitting[students_not_sitting.index(student)] = (student[0],student[1],student_object.gender)
            except:
                pass
    c1r1 = students[0]
    c1r2 = students[1]
    c2r1 = students[2]
    c2r2 = students[3]
    c3r1 = students[4]
    c3r2 = students[5]
    c4r1 = students[6]
    c4r2 = students[7]
    c1r11 = students[8]
    c1r21 = students[9]
    c2r11 = students[10]
    c2r21 = students[11]
    c3r11 = students[12]
    c3r21 = students[13]
    c4r11 = students[14]
    c4r21 = students[15]
    c1r12 = students[16]
    c1r22 = students[17]
    c2r12 = students[18]
    c2r22 = students[19]
    c3r12 = students[20]
    c3r22 = students[21]
    c4r12 = students[22]
    c4r22 = students[23]
    try:
        c1r1name_object = Student.objects.get(id=c1r1)
        c1r1name = c1r1name_object.firstName+" "+c1r1name_object.lastName
        c1r1gender = c1r1name_object.gender
    except:
        c1r1name = "Boş"
        c1r1gender = "Boş"
    try:
        c1r2name_object = Student.objects.get(id=c1r2)
        c1r2name = c1r2name_object.firstName+" "+c1r2name_object.lastName
        c1r2gender = c1r2name_object.gender
    except:
        c1r2name = "Boş"
        c1r2gender = "Boş"
    try:
        c2r1name_object = Student.objects.get(id=c2r1)
        c2r1name = c2r1name_object.firstName+" "+c2r1name_object.lastName
        c2r1gender = c2r1name_object.gender
    except:
        c2r1name = "Boş"
        c2r1gender = "Boş"
    try:
        c2r2name_object = Student.objects.get(id=c2r2)
        c2r2name = c2r2name_object.firstName+" "+c2r2name_object.lastName
        c2r2gender = c2r2name_object.gender
    except:
        c2r2name = "Boş"
        c2r2gender = "Boş"
    try:
        c3r1name_object = Student.objects.get(id=c3r1)
        c3r1name = c3r1name_object.firstName+" "+c3r1name_object.lastName
        c3r1gender = c3r1name_object.gender
    except:
        c3r1name = "Boş"
        c3r1gender = "Boş"
    try:
        c3r2name_object = Student.objects.get(id=c3r2)
        c3r2name = c3r2name_object.firstName+" "+c3r2name_object.lastName
        c3r2gender = c3r2name_object.gender
    except:
        c3r2name = "Boş"
        c3r2gender = "Boş"  
    try:
        c4r1name_object = Student.objects.get(id=c4r1)
        c4r1name = c4r1name_object.firstName+" "+c4r1name_object.lastName
        c4r1gender = c4r1name_object.gender
    except:
        c4r1name = "Boş"
        c4r1gender = "Boş"  
    try:
        c4r2name_object = Student.objects.get(id=c4r2)
        c4r2name = c4r2name_object.firstName+" "+c4r2name_object.lastName
        c4r2gender = c4r2name_object.gender
    except:
        c4r2name = "Boş"
        c4r2gender = "Boş"
    try:
        c1r11name_object = Student.objects.get(id=c1r11)
        c1r11name = c1r11name_object.firstName+" "+c1r11name_object.lastName
        c1r11gender = c1r11name_object.gender
    except:
        c1r11name = "Boş"
        c1r11gender = "Boş"
    try:
        c1r21name_object = Student.objects.get(id=c1r21)
        c1r21name = c1r21name_object.firstName+" "+c1r21name_object.lastName
        c1r21gender = c1r21name_object.gender
    except:
        c1r21name = "Boş"
        c1r21gender = "Boş"
    try:
        c2r11name_object = Student.objects.get(id=c2r11)
        c2r11name = c2r11name_object.firstName+" "+c2r11name_object.lastName
        c2r11gender = c2r11name_object.gender
    except:
        c2r11name = "Boş"
        c2r11gender = "Boş"
    try:
        c2r21name_object = Student.objects.get(id=c2r21)
        c2r21name = c2r21name_object.firstName+" "+c2r21name_object.lastName
        c2r21gender = c2r21name_object.gender
    except:
        c2r21name = "Boş"
        c2r21gender = "Boş"
    try:
        c3r11name_object = Student.objects.get(id=c3r11)
        c3r11name = c3r11name_object.firstName+" "+c3r11name_object.lastName
        c3r11gender = c3r11name_object.gender
    except:
        c3r11name = "Boş"
        c3r11gender = "Boş"
    try:
        c3r21name_object = Student.objects.get(id=c3r21)
        c3r21name = c3r21name_object.firstName+" "+c3r21name_object.lastName
        c3r21gender = c3r21name_object.gender
    except:
        c3r21name = "Boş" 
        c3r21gender = "Boş" 
    try:
        c4r11name_object = Student.objects.get(id=c4r11)
        c4r11name = c4r11name_object.firstName+" "+c4r11name_object.lastName
        c4r11gender = c4r11name_object.gender
    except:
        c4r11name = "Boş" 
        c4r11gender = "Boş" 
    try:
        c4r21name_object = Student.objects.get(id=c4r21)
        c4r21name = c4r21name_object.firstName+" "+c4r21name_object.lastName
        c4r21gender = c4r21name_object.gender
    except:
        c4r21name = "Boş"
        c4r21gender = "Boş"
    try:
        c1r12name_object = Student.objects.get(id=c1r12)
        c1r12name = c1r12name_object.firstName+" "+c1r12name_object.lastName
        c1r12gender = c1r12name_object.gender
    except:
        c1r12name = "Boş"
        c1r12gender = "Boş"
    try:
        c1r22name_object = Student.objects.get(id=c1r22)
        c1r22name = c1r22name_object.firstName+" "+c1r22name_object.lastName
        c1r22gender = c1r22name_object.gender
    except:
        c1r22name = "Boş"
        c1r22gender = "Boş"
    try:
        c2r12name_object = Student.objects.get(id=c2r12)
        c2r12name = c2r12name_object.firstName+" "+c2r12name_object.lastName
        c2r12gender = c2r12name_object.gender
    except:
        c2r12name = "Boş"
        c2r12gender = "Boş"
    try:
        c2r22name_object = Student.objects.get(id=c2r22)
        c2r22name = c2r22name_object.firstName+" "+c2r22name_object.lastName
        c2r22gender = c2r22name_object.gender
    except:
        c2r22name = "Boş"
        c2r22gender = "Boş"
    try:
        c3r12name_object = Student.objects.get(id=c3r12)
        c3r12name = c3r12name_object.firstName+" "+c3r12name_object.lastName
        c3r12gender = c3r12name_object.gender
    except:
        c3r12name = "Boş"
        c3r12gender = "Boş"
    try:
        c3r22name_object = Student.objects.get(id=c3r22)
        c3r22name = c3r22name_object.firstName+" "+c3r22name_object.lastName
        c3r22gender = c3r22name_object.gender
    except:
        c3r22name = "Boş" 
        c3r22gender = "Boş" 
    try:
        c4r12name_object = Student.objects.get(id=c4r12)
        c4r12name = c4r12name_object.firstName+" "+c4r12name_object.lastName
        c4r12gender = c4r12name_object.gender
    except:
        c4r12name = "Boş" 
        c4r12gender = "Boş" 
    try:
        c4r22name_object = Student.objects.get(id=c4r22)
        c4r22name = c4r22name_object.firstName+" "+c4r22name_object.lastName
        c4r22gender = c4r22name_object.gender
    except:
        c4r22name = "Boş"
        c4r22gender = "Boş"
    context = {
        'studentList':students_not_sitting,
        'sessions':sessions,
        'periods':periods,
        'classNames':classNames,
        'classLevels':classLevels,
        'media_url':settings.MEDIA_URL,
        'all_class_levels':all_class_levels,
        'c1r1':c1r1,
        'c1r2':c1r2,
        'c2r1':c2r1,
        'c2r2':c2r2,
        'c3r1':c3r1,
        'c3r2':c3r2,
        'c4r1':c4r1,
        'c4r2':c4r2,
        'c1r11':c1r11,
        'c1r21':c1r21,
        'c2r11':c2r11,
        'c2r21':c2r21,
        'c3r11':c3r11,
        'c3r21':c3r21,
        'c4r11':c4r11,
        'c4r21':c4r21,
        'c1r12':c1r12,
        'c1r22':c1r22,
        'c2r12':c2r12,
        'c2r22':c2r22,
        'c3r12':c3r12,
        'c3r22':c3r22,
        'c4r12':c4r12,
        'c4r22':c4r22,
        'c1r1name':c1r1name,
        'c1r2name':c1r2name,
        'c2r1name':c2r1name,
        'c2r2name':c2r2name,
        'c3r1name':c3r1name,
        'c3r2name':c3r2name,
        'c4r1name':c4r1name,
        'c4r2name':c4r2name,
        'c1r11name':c1r11name,
        'c1r21name':c1r21name,
        'c2r11name':c2r11name,
        'c2r21name':c2r21name,
        'c3r11name':c3r11name,
        'c3r21name':c3r21name,
        'c4r11name':c4r11name,
        'c4r21name':c4r21name,
        'c1r12name':c1r12name,
        'c1r22name':c1r22name,
        'c2r12name':c2r12name,
        'c2r22name':c2r22name,
        'c3r12name':c3r12name,
        'c3r22name':c3r22name,
        'c4r12name':c4r12name,
        'c4r22name':c4r22name,
        'c1r1gender':c1r1gender,
        'c1r2gender':c1r2gender,
        'c2r1gender':c2r1gender,
        'c2r2gender':c2r2gender,
        'c3r1gender':c3r1gender,
        'c3r2gender':c3r2gender,
        'c4r1gender':c4r1gender,
        'c4r2gender':c4r2gender,
        'c1r11gender':c1r11gender,
        'c1r21gender':c1r21gender,
        'c2r11gender':c2r11gender,
        'c2r21gender':c2r21gender,
        'c3r11gender':c3r11gender,
        'c3r21gender':c3r21gender,
        'c4r11gender':c4r11gender,
        'c4r21gender':c4r21gender,
        'c1r12gender':c1r12gender,
        'c1r22gender':c1r22gender,
        'c2r12gender':c2r12gender,
        'c2r22gender':c2r22gender,
        'c3r12gender':c3r12gender,
        'c3r22gender':c3r22gender,
        'c4r12gender':c4r12gender,
        'c4r22gender':c4r22gender,
            
    }
    
    return render(request, "clasess/cls-listSeat.html", context)
@login_required(login_url="/login/")
def classredirect(request,pk):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    level_list = []
    name_list = []
    for i in pk:
        try:
            i = int(i)
            i = str(i)
            level_list.append(i)
        except:
            name_list.append(i)
    level = ''.join(level_list)
    class_name = ''.join(name_list)
    class_name_object = ClassNames.objects.get(name=class_name)
    class_level_object = ClassLevels.objects.get(level=level)
    try:
        class_object = Classes.objects.get(className=class_name_object,level=class_level_object)
    except:
        class_object = Classes(className=class_name_object,level=class_level_object)
        class_object.save()
    try:
        student_list_object = (StudentList.objects.filter(className=class_object))[0]
        pk = student_list_object.id
    except:
        newstudentlist = StudentList(className = class_object,session = session,periods = period)
        newstudentlist.save()
        student_list_object = StudentList.objects.get(className=class_object)
        pk = student_list_object.id
    return redirect('classlist', pk=pk)
@login_required(login_url="/login/")
def classlist(request,pk):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    try:
        base_list = StudentList.objects.get(id=pk,session=session,periods=period)
    except:
        base_list = StudentList.objects.get(id=pk)
        try:
            base_list_object = StudentList.objects.get(session = session,periods = period,className=base_list.className)
        except:
            base_list_object = StudentList(session = session,periods = period,className=base_list.className)
            base_list_object.save()
        base_list = base_list_object
    students = list(base_list.students.all())
    for i in students:
        students[students.index(i)] = (str(int(students.index(i))+1),students[students.index(i)])
    class_name = str(base_list.className)
    level_list = []
    name_list = []
    for i in class_name:
        try:
            i = int(i)
            i = str(i)
            level_list.append(i)
        except:
            name_list.append(i)
    level = ''.join(level_list)
    class_name = ''.join(name_list)
    class_name_list = []
    class_name_list.append(level)
    class_name_list.append(class_name)
    class_name = "-".join(class_name_list)
    context = {
        'class':base_list,
        'sessions':sessions,
        "periods":periods,
        'all_class_levels':all_class_levels,
        'media_url':settings.MEDIA_URL,
        'students':students,
        'class_name':class_name
    }
    return render(request, "clasess/cls-class.html", context)