from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil,JobsTable,SessionPeriod,Period,Session


# class ProfilForm(forms.ModelForm):

#     class Meta:
#         model = Profil
#         fields = ('__all__')

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
    adress = forms.CharField(widget=forms.TextInput(attrs={
        'id':'adres',
        'class': 'form-control',
        'placeholder': 'Adres',
        'requirement':""
    }),required=False)
    TC = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'TC No'
    }),required=False)
    HESCode = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '____-____-_'
    }),required=False)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(attrs={
        'class': 'form-control',
        'placeholder': 'Dogum Günü'
    }),required=False)
    
   
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'image',
        
    }),required=False)
   
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Telefon No'
    }),required=False)
    
    CHOICES =[('Kız','Kız'),
              ('Erkek','Erkek'),
              ('Diger','Diğer'),
    ]
    gender = forms.ChoiceField( widget=forms.Select({'class':'form-control'}) , choices=CHOICES,required=False
        )
    isWorking = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-control',
        'placeholder': 'Calisiyor mu'
    }),required=False)
    
    job = forms.ModelChoiceField(queryset=JobsTable.objects.all(),widget=forms.Select({
        'class': ' form-control bg-grey',
        'placeholder': 'Meslek',
         
        }),required=False)
    
    class Meta:
        model = Profil
        fields =  ['adress',"TC",'phone','HESCode','gender',"isWorking",'image',"birthdate","job"]

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id':'username',
        'class': 'form-control',
        'placeholder': 'Kullanıcı Adı'
    }),required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id':'first_name',
        'class': 'form-control',
        'placeholder': 'Adınız'
    }),required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id':'last_name',
        'class': 'form-control',
        'placeholder': 'Soy adınız'
    }),required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id':'email',
        'class': 'form-control',
        'placeholder': 'Your Email'
    }),required=False)
   
    

    class Meta:
        model = User
        fields =  ['first_name',"last_name","email","username"]
        
class SessionForm(forms.ModelForm):
    session = forms.ModelChoiceField(queryset=Session.objects.all(),widget=forms.TextInput(attrs={
        'id':'session',
        'class': 'form-control',
    }),required=False)
    active = forms.BooleanField(widget=forms.TextInput(attrs={
        'id':'activeSession',
        'class': 'form-control',
    }),required=False)
    
    class Meta:
        model = Session
        fields =  ['session',"active"]