# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present RoboBusters
"""

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings
from apps.home.form import ProfilForm
from apps.home.models  import Profil,JobsTable
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .form import ProfilForm

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
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

def userShow(request):
    users = Profil.objects.all()
    context = {
        'Kullanicilar' : users,
        'media_url':settings.MEDIA_URL
    }
    
    return render(request,'home/usr-ogretmenler.html',context)

def post_update(request):
    pk=request.user.id
    post = get_object_or_404(Profil, id=1)
    
    form = ProfilForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        
        return HttpResponseRedirect('/')
    
    user = User.objects.get(id=1)
    detail = Profil.objects.get(user=user)
    jobs =  JobsTable.objects.all()
    form = ProfilForm(instance=post)
  
    context={
        'user':user,
        'detail':detail,
        'jobs':jobs,
        'form':form,
        'media_url':settings.MEDIA_URL
        }
    

    return render(request, "home/profil.html", context)


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
        'media_url':settings.MEDIA_URL
    }
    return render(request,'home/profil.html',context)


class ProfilView(FormView):
    template_name = 'profil.html'
    form_class = ProfilForm
    success_url = reverse_lazy('profil')
    #success_message = 'We received your request'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)