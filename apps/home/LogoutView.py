

from django import template
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from apps.authentication.forms import LoginForm
from apps.home.form import SignUpForm

def as_view(request):
    pass