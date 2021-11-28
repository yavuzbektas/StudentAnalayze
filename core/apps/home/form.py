from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil


class ProfilForm(forms.ModelForm):

    class Meta:
        model = Profil
        fields = ('__all__')

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-Type Password'
    }))

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']

class ProfilForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    TC = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'TC'
    }))
    HESCode = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'HES Code'
    }))
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'birthday'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    job = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'job'
    }))
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'address'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Phone'
    }))
    gender = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Gender'
    }))
    isWorking = forms.BooleanField()(widget=forms.CheckboxInput(attrs={
        'class': 'form-control',
        'placeholder': 'isWorking'
    }))

    class Meta:
        model = Profil
        fields =  ['first_name', 'last_name','TC', 'HES Code','username','email','isWorking','gender','job', 'phone', 'message']
