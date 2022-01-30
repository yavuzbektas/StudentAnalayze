# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present RoboBusters
"""

from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings
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
sessions = Session.objects.all()
periods = Period.objects.all()
all_class_levels = all_class_levels()

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index','sessions':sessions,"periods":periods,'all_class_levels':all_class_levels}

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
            formf =profile_form.save(commit=False)
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
        'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels
        }
    

    return render(request, "home/profil.html", context)

@login_required(login_url="/login/")
def userUpdate(request):
    id= request.user.id
    user = User.objects.get(id=id)
    detail = Profil.objects.get(user=user)
    jobs =  JobsTable.objects.all()
    form = ProfilForm()
    context={
        'user':user,
        'detail':detail,
        'jobs':jobs,
        'form':form,
        'media_url':settings.MEDIA_URL,
        'sessions':sessions,"periods":periods,'all_class_levels':all_class_levels
    }
    return render(request,'home/profil.html',context)

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
    
    
