from django.core.checks import messages
from django.http import request
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from account.forms import LoginForm, SignUpForm
"""login_view, register_user"""
def login_view(request):
       if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
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
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "home/deneme.html",{"form": form, "msg": msg, "success": success})
    #, 