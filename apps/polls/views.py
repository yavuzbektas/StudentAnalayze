# -*- encoding: utf-8 -*-

from django import template
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from django import template
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.urls import reverse

from apps.home.form import PostForm



# from .form import testForm


def validateHesCode(value):
    HesCodeRegex = RegexValidator(regex=r'^[0-9]{4}-?[0-9]{5}$', message="HES Code  must be entered in the format: 'Txxx-xxxx-x'. Up to 9  char allowed.")

def validatePhone(value):
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
    # y=str(value)
    # x=list(y)    
        
    # if len(x) != 10 :
    #     raise ValidationError(
    #         _('%(value)s 10 basasmaklı olmalı'),
    #         params={'value': value},
    #     )


def validateEven(value):
    y=str(value)
    x=list(y)
        
        
    if len(x) != 11:
        raise ValidationError(
            ('%(value)s 11 basasmaklı olmalı'),
            params={'value': value},
        )



def index(request):

    return render(request,'polls/index.html')
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



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

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
def formview(request):
     form = PostForm(request.POST or None, request.FILES or None)
     context = {
        'form': form
    }

     return render(request, "post/form.html", context)