from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil,JobsTable


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
        'class': 'form-control',
        'placeholder': 'Adres'
    }))
    TC = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'TC No'
    }))
    HESCode = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'HES No'
    }))
    
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'image'
    }))
   
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Telefon No'
    }))
    
    CHOICES =[('Kız','Kız'),
              ('Erkek','Erkek'),
              ('Diger','Diğer'),
    ]
    gender = forms.ChoiceField( widget=forms.RadioSelect({'class':'form-check'}) , choices=CHOICES
        )
    isWorking = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-control',
        'placeholder': 'Calisiyor mu'
    }),required=False)

    class Meta:
        model = Profil
        fields =  ['adress',"TC",'phone','HESCode','gender',"isWorking","email",'image']

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Kullanıcı Adı'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Adınız'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Soy adınız'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
   
    

    class Meta:
        model = User
        fields =  ['first_name',"last_name","email","username"]