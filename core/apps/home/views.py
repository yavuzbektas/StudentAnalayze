# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present RoboBusters
"""

from datetime import datetime,timedelta
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings
from apps.attendance.models import DailyAttendance, LessonPeriods
from apps.home.form import ProfilForm
from apps.home.models  import Profil,JobsTable,Session,Period,SessionPeriod
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .form import ProfilForm,UserForm,SessionForm
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from apps.classes.classes_for_sidebar import all_class_levels
from apps.student.views import sessionUpdate
from apps.student.models import Student,StudentList
from apps.classes.models import Classes

sessions = Session.objects.all()
periods = Period.objects.all()
all_class_levels = all_class_levels()


@login_required(login_url="/login/")
def index(request):
    sessionUpdate(request)    
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    students = StudentList.objects.filter(session=session,periods=period)
    girlsCount= StudentList.objects.filter(session=session,periods=period,students__gender='Kız')
    boysCount= StudentList.objects.filter(session=session,periods=period,students__gender='Erkek')
    teacherWCount= Profil.objects.filter(isWorking=True,gender='Kız')
    teacherMCount= Profil.objects.filter(isWorking=True,gender='Erkek')
    teachers=Profil.objects.filter(isWorking=True)
    today = datetime.today().date()
    now = datetime.now().time()
    first_lesson_absent_list_att = list(DailyAttendance.objects.filter(day=today,session=session,periods=period))
    first_lesson_absent_list_att_remove = []
    for student in first_lesson_absent_list_att:
        if (str(student.lesPeriod.lessName) != "1.Ders"):
            first_lesson_absent_list_att_remove.append(student)
    for student in first_lesson_absent_list_att_remove:
        first_lesson_absent_list_att.remove(student)
    first_lesson_absent_list_students = []
    for student in first_lesson_absent_list_att:
        first_lesson_absent_list_students.append(student.student)
    for student in first_lesson_absent_list_students:
        for class_name in StudentList.objects.all():
            for student_object in class_name.students.all():
                if student_object == student:
                    className_first = str(class_name.className)
                    level_list = []
                    name_list = []
                    for i in className_first:
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
                    class_name_list.append("-")
                    class_name_list.append(class_name)
                    className = "".join(class_name_list)
                    first_lesson_absent_list_students[first_lesson_absent_list_students.index(student)] = (student,className,className_first)
    today_absent_list_att = list(DailyAttendance.objects.filter(day=today,session=session,periods=period))
    day_length = 0
    lesson_periods = LessonPeriods.objects.filter(session=session,periods=period)
    for lesson_period in lesson_periods:
        time_object = datetime.strptime(lesson_period.lesPeriod.split("-")[1], '%H:%M').time()
        if now > time_object:
            day_length += 1
    today_absent_list_students = []
    for student_att in today_absent_list_att:
        student_object = student_att.student
        student_object_counter = 0
        for student in today_absent_list_att:
            if student.student == student_object:
                student_object_counter += 1
        if((student_object_counter >= day_length) and (student_object not in today_absent_list_students)):
            today_absent_list_students.append(student_object)
    for student in today_absent_list_students:
        for class_name in StudentList.objects.all():
            for student_object in class_name.students.all():
                if student_object == student:
                    className_first = str(class_name.className)
                    level_list = []
                    name_list = []
                    for i in className_first:
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
                    class_name_list.append("-")
                    class_name_list.append(class_name)
                    className = "".join(class_name_list)
                    today_absent_list_students[today_absent_list_students.index(student)] = (student,className,className_first)
    week_dates = [today + timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
    week_absent_list_students = []
    for i in week_dates:
        if week_dates.index(i) == 0:
            day_name_str = "Pazartesi"
        elif week_dates.index(i) == 1:
            day_name_str = "Salı"
        elif week_dates.index(i) == 2:
            day_name_str = "Çarşamba"
        elif week_dates.index(i) == 3:
            day_name_str = "Perşembe"
        elif week_dates.index(i) == 4:
            day_name_str = "Cuma"
        elif week_dates.index(i) == 5:
            day_name_str = "Cumartesi"
        else:
            day_name_str = "Pazar"
        week_dates[week_dates.index(i)] = (week_dates[week_dates.index(i)],day_name_str)
    day_length = len(lesson_periods)
    for day,day_name_str in week_dates:
        day_absent_list_att = list(DailyAttendance.objects.filter(day=day,session=session,periods=period))
        day_absent_list_students = []
        for student_att in day_absent_list_att:
            student_object = student_att.student
            student_object_counter = 0
            for student in day_absent_list_att:
                if student.student == student_object:
                    student_object_counter += 1
            if((student_object_counter == day_length) and (student_object not in day_absent_list_students)):
                day_absent_list_students.append(student_object)
        if day_absent_list_students:
            for student in day_absent_list_students:
                week_absent_list_students.append((student,day_name_str))
    for student in week_absent_list_students:
        for class_name in StudentList.objects.all():
            for student_object in class_name.students.all():
                if student_object == student[0]:
                    className_first = str(class_name.className)
                    level_list = []
                    name_list = []
                    for i in className_first:
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
                    class_name_list.append("-")
                    class_name_list.append(class_name)
                    className = "".join(class_name_list)
                    week_absent_list_students[week_absent_list_students.index(student)] = (student[0],student[1],className,className_first)
    context = {
        'segment': 'index',
        'students':students,
        'sessions':sessions,
        "periods":periods,
        'girlsCount':girlsCount,
        'teachers':teachers,
        'teacherWCount':teacherWCount,
        'teacherMCount':teacherMCount,
        'boysCount':boysCount,
        'all_class_levels':all_class_levels,
        'first_lesson_absent':first_lesson_absent_list_students,
        'today_absent':today_absent_list_students,
        'thisWeek_absent':week_absent_list_students,
        'media_url':settings.MEDIA_URL
        }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        pass
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def profilShowList(request):
    jobs =  JobsTable.objects.all()
    
    jobname = request.GET.get("jobname")
    if jobname ==None or jobname =="0":
        profilList = Profil.objects.all()
    else:
        
        profilList = Profil.objects.filter(job__name=jobname)
    context = {
        'Kullanicilar' : profilList,
        'media_url':settings.MEDIA_URL,
        'jobs':jobs,
        'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels
    }
    
    return render(request,'home/usr-ogretmenler.html',context)

@login_required(login_url="/login/")
def profilView(request,pk=None):
    detail = Profil.objects.get(id=pk)
    
    context={
        
        'detail':detail,
        
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels
        }
    

    return render(request, "home/profilView.html", context)


@login_required(login_url="/login/")
def profilUpdate(request,pk=None):
    if pk==None:
        pk=request.user.id
    user = User.objects.get(id=pk)
    post = Profil.objects.get(user=user)
    
    jobs =  JobsTable.objects.all()
    
    profile_form = ProfilForm(request.POST,request.FILES, instance=post)
    user_form = UserForm(request.POST, instance=user)
    if request.method == 'POST':
        if profile_form.is_valid() and user_form.is_valid():
            formf =profile_form.save()
            userf= user_form.save()
            formf.user=userf
            formf.save()
            
            return HttpResponseRedirect('/view/'+str(post.id))
        elif profile_form.errors :
            print("Profil form da hatalar var" , profile_form.errors.as_text())
            
        elif user_form.errors :
            print("User form da hatalar var",user_form.errors.as_text())
            
    profile_form = ProfilForm(instance=post)
    user_form = UserForm(instance=user)
    context={
        'user':user,
        'detail':post,
        'jobs':jobs,
        'profile_form':profile_form,
        'user_form':user_form,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,
        "periods":periods,
        'all_class_levels':all_class_levels
        }
    

    return render(request, "home/profil.html", context)


@login_required(login_url="/login/")
def profilDelete(request, pk):
    
    post = get_object_or_404(Profil, id=pk)
    profil = Profil.objects.get(id=pk)
    user = User.objects.get(id=profil.user.id)
    if not request.user.is_authenticated:
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    if request.method == 'GET':
        post.delete()
        user.delete()
        return redirect('/usr-ogretmenler.html')
    
    context={
        'form': profil
    }
    
    

@login_required(login_url="/login/")
def issuperUser(request,pk):
    
    User = get_user_model()
    user = User.objects.get(id=pk)
    if request.method == 'GET':
        if user.is_superuser :
            user.is_staff = False
            user.is_admin = False
            user.is_superuser = False
            
        else:
            user.is_staff = True
            user.is_admin = False
            user.is_superuser = True
        user.save()
        return redirect('/usr-ogretmenler.html')
    context={
        'form': user
    }
    
    
