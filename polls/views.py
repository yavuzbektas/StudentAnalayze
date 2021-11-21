from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

def validateHesCode(value):
    HesCodeRegex = RegexValidator(regex=r'^[0-9]{4}-?[0-9]{5}$', message="HES Code  must be entered in the format: 'Txxx-xxxx-x'. Up to 9  char allowed.")

def validate_evenz(value):
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
    # y=str(value)
    # x=list(y)    
        
    # if len(x) != 10 :
    #     raise ValidationError(
    #         _('%(value)s 10 basasmaklı olmalı'),
    #         params={'value': value},
    #     )




def validate_even(value):
    y=str(value)
    x=list(y)
        
        
    if len(x) != 11:
        raise ValidationError(
            _('%(value)s 11 basasmaklı olmalı'),
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