
from cgi import print_environ
from http.client import HTTPResponse
from multiprocessing import context
from pydoc import classname
from urllib import request
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from apps.attendance.views import sessionUpdate
from django.views.generic.list import ListView
from apps.classes.models import ClassLevels, ClassNames
from apps.home.models import Period, Session,Profil
from apps.lessons.form import LessonClassListForm, lessonForm
from apps.lessons.models import Lesson, LessonClassList
from apps.student.models import StudentList

# Create your views here.

@login_required(login_url="/login/")
def LessonAdd(request):
    

    sessionUpdate(request)
    

    lesson_form = lessonForm(request.POST,request.FILES)
  
    
    
    if request.method == 'POST':
        
        
                  
        if lesson_form.is_valid():
            try:
                formf1 =lesson_form.save()
                print(formf1)
            except Exception as err:
                print(err)
                return redirect('/')
                
               
            
            
            return redirect('student-list')
            
        
        
    context={
       
        'lesson_form':lesson_form,
        
       
        }
    return render(request, "lesson/lesson-add.html", context)
@login_required(login_url="/login/")
def LessonAdd(request):
    

    sessionUpdate(request)
    
    lesson_form = lessonForm(request.POST,request.FILES)
    if request.method == 'POST':
        
        
                  
        if lesson_form.is_valid():
            try:
                formf1 =lesson_form.save()
                print(formf1)
            except Exception as err:
                print(err)
                return redirect('/')
                
               
            
            
            return redirect('student-list')
            
        
        
    context={
       
        'lesson_form':lesson_form,
        
       
        }
    return render(request, "lesson/lesson-add.html", context)
@login_required(login_url="/login/")
def LessonClassListAdd(request):
    

    sessionUpdate(request)
    
    fromdata = LessonClassListForm(request.POST,request.FILES)        
    
    if request.method == 'POST':
        if fromdata.is_valid():
            
            try:
                fromdata.save()
                return redirect('/lessons/lessons/list/')
                
               
            except Exception as err:
                print(err)
                return redirect('/lessons/lessons/list/')
            
            
            
        
        
    context={
       
        'lesson_form':fromdata,
        
       
        }
    return render(request, "lesson/DerslikAdd.html", context)
class LessonClassListList(ListView):
    model=LessonClassList
    template_name="lesson/lesson-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['classLevels']=ClassLevels.objects.all()
        context['sessions']=Session.objects.all()
        context['periods']=Period.objects.all()
        context['classNames']=ClassNames.objects.all()
        return context
    def get_queryset(self):
        queryset = {"lessonClassList": LessonClassList.objects.all()}
        sessionUpdate(self.request)
        session=Session.objects.get(active=True)
        period=Period.objects.get(active=True)
        className = self.request.GET.get("className")
        classLevel = self.request.GET.get("classLevel")
        
        query={}
        
        
        if className!="0" and className!=None:
            
            query['className__className__className__name__contains']=className
        else:
            query['className__className__className__name__contains']=""
            
     
        if classLevel!="0" and classLevel!=None:
           
            query['className__className__level__level__contains']=classLevel
          
        else:
            query['className__className__level__level__contains']=""
            
            
        query["className__session__session__contains"]=session
        query["className__periods__period__contains"]=period
        
        queryset = {"lessonClassList": LessonClassList.objects.filter(**query)}  
        print(LessonClassList.objects.filter(**query))        
        
        return queryset 

# class StudentListDetailView(ListView):
    
#     model = StudentList
#     template_name="clasess/cls-list.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         context['classLevels']=ClassLevels.objects.all()
#         context['sessions']=Session.objects.all()
#         context['periods']=Period.objects.all()
#         context['classNames']=ClassNames.objects.all()
#         context['studentlist']=StudentList.objects.all()
        
#         return context
#     def get_queryset(self):
#         queryset = {"studentlist": StudentList.objects.all()}
#         sessionUpdate(self.request)
    
#         session=Session.objects.get(active=True)
#         period=Period.objects.get(active=True)
#         className = self.request.GET.get("className")
#         classLevel = self.request.GET.get("classLevel")
#         query={}
        
           
#         if className!="0" and className!=None:
#             query['className__className__name__contains']=className
            
#         else:
#             query['className__className__name__contains']=""
           
#         if classLevel!="0" and classLevel!=None:
#             query['className__level__level__contains']=classLevel
          
#         else:
#             query['className__level__level__contains']=""
            
            
#         query["session__session__contains"]=session
#         query["periods__period__contains"]=period
#         try:
#             queryset = {"studentlist": StudentList.objects.filter(**query)}  
            
#         except:
#             print("sorgu hatası") 
#         return queryset '''