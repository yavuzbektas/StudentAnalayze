from django.core.checks import messages
from django.http import request
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm, SignUpForm
"""login_view, register_user"""
def login_view(request):
       if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                        password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'Disabled Account')

            else:
                messages.info(request, 'Check Your Username and Password')

        else:
            form = LoginForm()

        return render(request, 'login.html', {'form':form})
    
    


def register_user(request):
       if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created, You can LOGIN')
            return redirect('login')
    
        else:
            form = SignUpForm()

        return render(request, 'register.html', {'form':form})


def user_logout(request):
        logout(request)
        return redirect('index')
    #, 