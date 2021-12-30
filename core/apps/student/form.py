from django import forms
from apps.home.models import Session
from .models import Student,StudentList,Parent,MiddleSchool

class StudentForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'id':'firstName',
        'class': 'form-control',
        'placeholder': 'Adınız',
    }),required=False)
    lastName = forms.CharField(widget=forms.TextInput(attrs={
        'id':'lastName',
        'class': 'form-control',
        'placeholder': 'Soy Adınız',
        
    }),required=False)
    
    TC = forms.CharField(widget=forms.TextInput(attrs={
        'id':'TC',
        'class': 'form-control',
        'placeholder': 'TC No'
    }),required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'id':'phone',
        'class': 'form-control',
        'placeholder': 'Telefon No'
    }),required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={
        'id':'address',
        'class': 'form-control',
        'placeholder': 'Adres',
        
    }),required=False)
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'id':'status',
        'class': 'form-control',
        'placeholder': 'Ayrıldı Mı?'
    }),required=False)
    middleSchool = forms.ModelChoiceField(queryset=MiddleSchool.objects.all(),widget=forms.Select({
        'id':'middleSchool',
        'class': ' form-control',
        'placeholder': 'Orta Okul',
         
        }),required=False)
    number = forms.CharField(widget=forms.TextInput(attrs={
        'id':'number',
        'class': 'form-control',
        'placeholder': 'Okul No'
    }),required=False)
    session = forms.ModelChoiceField(queryset=Session.objects.all(),widget=forms.Select({
        'id':'session',
        'class': ' form-control',
        'placeholder': 'sezon',
         
        }),required=False)
    health = forms.CharField(widget=forms.TextInput(attrs={
        'id':'health',
        'class': 'form-control',
        'placeholder': 'Sağlık Bilgisi',
        
    }),required=False)
    HESCode = forms.CharField(widget=forms.TextInput(attrs={
        'id':'hescode',
        'class': 'form-control',
        'placeholder': '____-____-_'
    }),required=False)
    birtdate = forms.DateField(widget=forms.SelectDateWidget(attrs={
        'id':'birtdate',
        'class': 'form-control',
        'placeholder': 'Dogum Günü'
    }),required=False)
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id':'email',
        'class': 'form-control',
        'placeholder': 'Email'
    }),required=False)
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'id':'TC',
        'class': 'form-control',
        'placeholder': 'Resim',
        
    }),required=False)
   
    CHOICES =[('Kız','Kız'),
              ('Erkek','Erkek'),
              ('Diger','Diğer'),
    ]
    gender = forms.ChoiceField( widget=forms.Select({'class':'form-control'}) , choices=CHOICES,required=False
        )
    
    
    
    class Meta:
        model = Student
        fields =  ['firstName','lastName','health','address',"TC",'phone','HESCode','gender',"status",'image',"birtdate","email",'middleSchool']
