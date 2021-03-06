import copy
import os
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Student,StudentList,Parent
from django.conf import settings
from .filter import StudentFilter
from django.conf import settings
from django.views.generic.list import ListView
from ..classes.models import ClassLevels,Classes,ClassNames
from ..home.models import Session,Period
from django.views.generic.detail import SingleObjectMixin
from .form import ParentForm, StudentForm,StudentListForm
from django.http import Http404, HttpResponse
from .resources import StudentResource
from tablib import Dataset
from xlrd import open_workbook
from apps.classes.classes_for_sidebar import all_class_levels
sessions = Session.objects.all()
periods = Period.objects.all()
all_class_levels = all_class_levels()
# Create your views here.
# excel_app/views.py
import xlwt
from django.http import HttpResponse

import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User

# Super User - admin - password



# writing to existing workbook using xlwt 
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd

import os

def export(request):
    
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'
        
        path = os.path.dirname(__file__)
        file = os.path.join(path, 'sample.xls')

        rb = open_workbook(file, formatting_info=True)
        r_sheet = rb.sheet_by_index(0)

        wb = copy(rb)
        ws = wb.get_sheet(0)

        row_num = 2 # index start from 0
        rows = Student.objects.all().values_list('firstName', 'lastName','HESCode', 'TC', 'email','birtdate')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num])
        
        # wb.save(file) # will replace original file
        # wb.save(file + '.out' + os.path.splitext(file)[-1]) # will save file where the excel file is
        wb.save(response)
        return response
        # return render(request,'student/export',context)
    
def studentImport(request):
    sessionUpdate(request)
    
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    
    query={}
    query2={}
    query["studentlist__session__session__contains"]=session
    query["studentlist__periods__period__contains"]=period
    students=Student.objects.filter(**query).distinct()
      
    if request.method == 'POST':
        dataset = Dataset() 
        new_students={} 
        newStudentlist=[]
        student={}         
        recordstatus=0 
        if 'import' in request.POST:
            try:
                new_students = dataset.load(request.FILES['myfile'].read(),format='xlsx')
            except:
                pass
            
            if new_students:
                for index in range(len(new_students)):
                    student={}
                    try: 
                        Student.objects.get(TC=new_students['TC'][index])
                        print("This student has already been recorded")
                        student['recordStatus']="Zaten Kay??tl??"
                        recordstatus=4 
                    except Exception as err:
                        newStudent = Student(
                            firstName=new_students['firstName'][index],lastName=new_students['lastName'][index],TC=new_students['TC'][index],
                            phone=new_students['phone'][index],address=new_students['address'][index],HESCode=new_students['HESCode'][index],
                            birtdate=new_students['birtdate'][index],health=new_students['health'][index],email=new_students['email'][index],
                            gender=new_students['gender'][index],number=new_students['number'][index],
                            )
                        newStudent.save() 
                        
                        query2['className__className__name__contains']=new_students['className'][index]
                        query2['className__level__level__contains']=new_students['classLevel'][index]
                        studentlist= StudentList.objects.get(**query2) .students.add(newStudent)
                        #StudentList.objects.get(className=ClassName(name=new_students['className'][index]),session=session,periods=period)
                        student['recordStatus']="Kaydedildi"
                        student['firstName']=new_students['firstName'][index]
                        student['TC']=new_students['TC'][index]
                        student['lastName']=new_students['lastName'][index]
                        student['phone']=new_students['phone'][index]
                        student['address']=new_students['address'][index]
                        student['HESCode']=new_students['HESCode'][index]
                        student['health']=new_students['health'][index]
                        student['birtdate']=new_students['birtdate'][index]
                        student['email']=new_students['email'][index]
                        student['gender']=new_students['gender'][index]
                        student['number']=new_students['number'][index]
                        student['className']=new_students['className'][index]
                        student['classLevel']=new_students['classLevel'][index]
                        recordstatus=5 
                        newStudentlist.append(student)    
            else:
                recordstatus=1              
        
        
        if 'load' in request.POST: 
            try:
                new_students = dataset.load(request.FILES['myfile'].read(),format='xlsx')
            except:
                pass
            if new_students:
                  
                for index in range(len(new_students)):
                    student={}
                    try: 
                        Student.objects.get(TC=new_students['TC'][index])
                        student['recordStatus']="Zaten Kay??tl??"
                        print("This student has already been recorded")
                        
                    except Exception as err:
                        student['recordStatus']="Kaydedilecek"
                        
                    try:
                        
                        student['firstName']=new_students['firstName'][index]
                        student['TC']=new_students['TC'][index]
                        student['lastName']=new_students['lastName'][index]
                        student['phone']=new_students['phone'][index]
                        student['address']=new_students['address'][index]
                        student['HESCode']=new_students['HESCode'][index]
                        student['health']=new_students['health'][index]
                        student['birtdate']=new_students['birtdate'][index]
                        student['email']=new_students['email'][index]
                        student['gender']=new_students['gender'][index]
                        student['number']=new_students['number'][index]
                        student['className']=new_students['className'][index]
                        student['classLevel']=new_students['classLevel'][index]
                        newStudentlist.append(student) 
                        recordstatus=2   
                    except:
                        recordstatus=3
            else:
                recordstatus=1      
        
        context={
        'studentlist':newStudentlist,
        'sessions':sessions,
        'periods':periods,
        'students':students,
        'recordStatus':recordstatus
        
        }
         
        return render(request, 'student/std-import.html',context)
                 
        
    context={"sessions":sessions,"periods":periods}

    return render(request, 'student/std-import.html',context)
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
            newPeriod =request.GET.get("periodID")
        except:
            pass
            print("Bu periyot yoktur")
            newPeriod =request.GET.get(id=0)
            
        
        print("Yeni Period  : ",newPeriod )
        newPeriod  = Period.objects.get(period=newPeriod )
        newPeriod.active=True
        newPeriod.save()

@login_required(login_url="/login/")
def parentUpdate(request,pk):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)  
    parent=Parent.objects.get(id=pk)
    student=Student.objects.all()
    parent_Form = ParentForm(request.POST,request.FILES,instance=parent)
    student_form = StudentForm(request.POST,request.FILES)
    
    
    getStudentList = StudentList.objects.filter(session=session,periods=period)
    if request.method == 'POST':
       
        if parent_Form.is_valid() :
            try:
                 
               instance= parent_Form.save()
               print(instance)
               return redirect('/student/add')  
            except Exception as err:
                print(err)
                return redirect('/student/add') 
                
               
            
            
            
            
        elif student_form.errors :
            print("form da hatalar var" , student_form.errors.as_text())
        elif parent_Form.errors :
            print("form da hatalar var" , parent_Form.errors.as_text())
        else:
            print("false")
    
    context={
        'ParentForm':parent_Form,
        'student_form':student_form,
        'studentListForm':student,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods,
        'allClassList':getStudentList,
        'all_class_levels':all_class_levels
       
        }
    return render(request, "student/std-parentUpdate.html", context)

@login_required(login_url="/login/")
def parentAdd(request):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)  
    
    student=Student.objects.all()
    parent_Form = ParentForm(request.POST,request.FILES)
    student_form = StudentForm(request.POST,request.FILES)
    
    getStudentList = StudentList.objects.filter(session=session,periods=period)
    if request.method == 'POST':
        
        if parent_Form.is_valid() :
            try:
                 
               instance= parent_Form.save()
               print(instance)
               return redirect('/student/add')  
            except Exception as err:
                print(err)
                return redirect('/student/add') 
                
               
            
            
            
            
        elif student_form.errors :
            print("form da hatalar var" , student_form.errors.as_text())
        elif parent_Form.errors :
            print("form da hatalar var" , parent_Form.errors.as_text())
        else:
            print("false")
    
    context={
        'parent_Form':parent_Form,
        'student_form':student_form,
        'studentListForm':student,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods,
        'allClassList':getStudentList,
        'all_class_levels':all_class_levels
       
        }
    return render(request, "student/std-ParentAdd.html", context)

@login_required(login_url="/login/")
def studentAdd(request):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)  
    parents=Parent.objects.all()

    student_form = StudentForm(request.POST,request.FILES)
    studentListForm = StudentListForm(request.POST,request.FILES)
    getStudentList = StudentList.objects.filter(session=session,periods=period)
    
    
    if request.method == 'POST':
        print(student_form.errors)
        if student_form.is_valid() and studentListForm.is_valid() :
            try:
                formf1 =student_form.save()
                formf1.firstName = (str(formf1.firstName).lower()).capitalize()
                formf1.lastName = (str(formf1.lastName).lower()).capitalize()
                formf1.save()
                newclassNameID = request.POST.get("classNameSelect")
                newclass = StudentList.objects.get(id=newclassNameID,session=session,periods=period)
                parentazi=request.POST.getlist("parentFormSelect")
                newclass.students.add(formf1)

                newclass.save() 
                
                for parenta in  parentazi:
                    print(parenta)
                    parent=Parent.objects.get(id=int(parenta))
                    parent.student.add(formf1)
                    
                
                
            except Exception as err:
                print(err)
                return redirect('/')
                
               
            
            
            return redirect('student-list')
        
        
    context={
       
        'parents':parents,
        'student_form':student_form,
        'studentListForm':studentListForm,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods,
        'allClassList':getStudentList,
        'all_class_levels':all_class_levels
       
        }
    return render(request, "student/std-add.html", context)

@login_required(login_url="/login/")
def studentUpdate(request,pk=None):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)    
    getStudentList = StudentList.objects.filter(session=session,periods=period).order_by("className")
    parents=Parent.objects.all()
    try:
        
        student = Student.objects.get(id=pk)
        oldclass = StudentList.objects.get(students=student,session=session,periods=period)
        
        
        if request.method == 'POST':
            student_form = StudentForm(request.POST,request.FILES, instance=student)
            if student_form.is_valid():
                newclassNameID = request.POST.get("classNameSelect")
                newclass = StudentList.objects.get(id=newclassNameID,session=session,periods=period)
                parentazi=request.POST.getlist("parentFormSelect")
                student_form.save()
                
                if oldclass.className != newclass.className or oldclass.session.session!=newclass.session.session :
                     
                    newclass.students.add(student)
                    oldclass.students.remove(student)
                return redirect('student-list')
                
            elif student_form.errors :
                print("Profil form da hatalar var" , student_form.errors.as_text())
            else:
                print("false")
    except Exception as err:
        print(err)
        context={
        
        'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels
        }
        return render(request, "student/std-Update.html", context)
    
    student_form = StudentForm(instance=student)
    
    birtdate = str(student.birtdate)

    context={
        'student':student,
        'stdClassName':oldclass,
        'allClassList':getStudentList,
        'student_form':student_form,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods,
        'birtdate':birtdate,
        'parents':parents,
        'all_class_levels':all_class_levels
        }
    return render(request, "student/std-Update.html", context)

@login_required(login_url="/login/")
def studentView(request,pk=None):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    try:
        student = Student.objects.get(id=pk)
        className = StudentList.objects.get(students=student,session=session,periods=period)
    except:
        context={
        
        'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels
        }
        return render(request,"student/std-list.html",context)
    context={
        'student':student,
        'studentclassName':className,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods,
        'all_class_levels':all_class_levels
        }
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
        "Kullanc?? Ad??" : "firstName",
        "Kullan??c?? Soyad??" : "lastName",
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
        'media_url':settings.MEDIA_URL,
        'all_class_levels':all_class_levels
    }
    
    return render(request, "student/std-list.html", context)

@login_required(login_url="/login/")
def studentDelete(request,pk):
    
    student = Student.objects.get(id=pk)
    if not request.user.is_authenticated:
        # E??er kullan??c?? giri?? yapmam???? ise hata sayfas?? g??nder
        return Http404()

    if request.method == 'GET':
        student.delete()
        return redirect('/')
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    
    return render(request, "student/std-list.html", context)

@login_required(login_url="/login/")
def studentIndex(request):
    context={'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    return render(request, "student/std-profile.html", context)

class StudentListView(ListView):
    template_name = 'student/std-list.html'
    model = Student

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['classLevels']=ClassLevels.objects.all()
        context['sessions']=Session.objects.all()
        context['periods']=Period.objects.all()
        context['classNames']=ClassNames.objects.all()
        context['media_url'] =settings.MEDIA_URL
        context['all_class_levels']=all_class_levels
        
        return context
    def get_queryset(self):
        queryset = {"studentlist": StudentList.objects.all()}
        
        sessionUpdate(self.request)
    
        session=Session.objects.get(active=True)
        period=Period.objects.get(active=True)
        className = self.request.GET.get("className")
        classLevel = self.request.GET.get("classLevel")
        if className==None:
            className="A"
        if classLevel==None:
            classLevel="9"    
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
            
        if classLevel=="0" and className=="0": 
            queryset = {"students": Student.objects.all().distinct(),"studentlist": StudentList.objects.all()}  
            return queryset
            
            
            
        else:
            query["studentlist__session__session__contains"]=session
            query["studentlist__periods__period__contains"]=period
            query2["session__session__contains"]=session
            query2["periods__period__contains"]=period
        try:
            queryset = {"students": Student.objects.filter(**query).distinct(),"studentlist": StudentList.objects.filter(**query2)}  
            
        except:
            print("sorgu hatas??")
            

        return queryset

