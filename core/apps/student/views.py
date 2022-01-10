from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Student,StudentList
from django.conf import settings
from .filter import StudentFilter
from django.conf import settings
from django.views.generic.list import ListView
from ..classes.models import ClassLevels,Classes,ClassNames
from ..home.models import Session,Period
from django.views.generic.detail import SingleObjectMixin
from .form import StudentForm,StudentListForm
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
def studentAdd(request):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)    
    getStudentList = StudentList.objects.filter(session=session,periods=period)
    student_form = StudentForm(request.POST,request.FILES)
    studentListForm = StudentListForm(request.POST,request.FILES)
    if request.method == 'POST':
        if student_form.is_valid() and studentListForm.is_valid():
            formf1 =student_form.save()
            studentListForm.students =formf1
            studentListForm.periods =period
            studentListForm.session =session
            studentListForm.save()
            print(studentListForm)
            return redirect('student-list')
            
        elif student_form.errors :
            print("form da hatalar var" , student_form.errors.as_text())
        elif studentListForm.errors :
            print("form da hatalar var" , studentListForm.errors.as_text())
        else:
            print("false")
    
    context={
        'student_form':student_form,
        'studentListForm':studentListForm,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods
        }
    return render(request, "student/std-add.html", context)


@login_required(login_url="/login/")
def studentUpdate(request,pk=None):
    sessionUpdate(request)
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)    
    
    try:
        
        student = Student.objects.get(id=pk)
        className = StudentList.objects.get(students=student,session=session,periods=period)
        student_form = StudentForm(request.POST,request.FILES, instance=student)
        
        if request.method == 'POST':
            student_form.save()
            if student_form.is_valid():
                formf =student_form.save()
                
                return redirect('student-list')
                
            elif student_form.errors :
                print("Profil form da hatalar var" , student_form.errors.as_text())
            else:
                print("false")
    except:
        context={
        
        'sessions':sessions,"periods":periods
        }
        return render(request, "student/std-Update.html", context)
    
    student_form = StudentForm(instance=student)
    birtdate = str(student.birtdate)

    context={
        'student':student,
        'className':className,
        'student_form':student_form,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods,
        'birtdate':birtdate,
        
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
def studentDelete(request,pk):
    
    student = Student.objects.get(id=pk)
    if not request.user.is_authenticated:
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    if request.method == 'GET':
        student.delete()
        return redirect('/')
    context={'sessions':sessions,"periods":periods}
    
    return render(request, "student/std-list.html", context)

@login_required(login_url="/login/")
def studentIndex(request):
    context={'sessions':sessions,"periods":periods}
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
            
        query["studentlist__session__session__contains"]=session
        query["studentlist__periods__period__contains"]=period
        query2["session__session__contains"]=session
        query2["periods__period__contains"]=period
        try:
            queryset = {"students": Student.objects.filter(**query).distinct(),"studentlist": StudentList.objects.filter(**query2)}  
            
        except:
            print("sorgu hatası")
            

        return queryset

