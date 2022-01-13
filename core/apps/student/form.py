from django import forms
from apps.home.models import Session,Period,Profil
from apps.classes.models import  Classes,ClassLevels,ClassNames
from .models import Student,StudentList,Parent,MiddleSchool,Period
from django.contrib.admin.widgets import AdminDateWidget
class StudentForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'id':'firstName_std',
        'class': 'form-control',
        'placeholder': 'Adınız',
    }),required=False)
    lastName = forms.CharField(widget=forms.TextInput(attrs={
        'id':'lastName_std',
        'class': 'form-control',
        'placeholder': 'Soy Adınız',
        
    }),required=False)
    
    TC = forms.CharField(widget=forms.TextInput(attrs={
        'id':'TC_std',
        'class': 'form-control',
        'placeholder': 'TC No'
    }),required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'id':'phone_std',
        'class': 'form-control',
        'placeholder': 'Telefon No'
    }),required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={
        'id':'address_std',
        'rows':'3' ,
        'cols':'30' ,
        'class': 'form-control',
        'placeholder': 'Adres',
        
    }),required=False)
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'id':'status_std',
        'class': 'form-control mx-2',
        'placeholder': 'Ayrıldı Mı?',
        'data-toggle':'toggle',
        'data-on':'AKTIF' ,
        'data-off':'AYRILDI' ,
        'data-onstyle':'success' ,
        'data-offstyle':'danger'
    }),required=False)
    middleSchool = forms.ModelChoiceField(queryset=MiddleSchool.objects.all(),widget=forms.Select({
        'id':'middleSchool_std',
        'class': ' form-control',
        'placeholder': 'Orta Okul',
         
        }),required=False)
    number = forms.CharField(widget=forms.TextInput(attrs={
        'id':'number_std',
        'class': 'form-control',
    }),required=False)
    session = forms.ModelChoiceField(queryset=Session.objects.all(),widget=forms.Select({
        'id':'session_std',
        'class': ' form-control',
        'placeholder': 'sezon',
         
        }),required=False)
    health = forms.CharField(widget=forms.Textarea(attrs={
        'id':'health_std',
        'rows':'3' ,
        'cols':'30' ,
        'class': 'form-control',
        'placeholder': 'Sağlık Bilgisi',
        
    }),required=False)
    HESCode = forms.CharField(widget=forms.TextInput(attrs={
        'id':'hescode_std',
        'class': 'form-control',
        'placeholder': '____-____-_'
    }),required=False)
    birtdate = forms.DateField(widget=forms.DateInput(attrs={
        'id':'birtdate_std',
        'type':'date',
        'class': 'form-control datepicker',
        'placeholder': 'Dogum Günü'
    }),required=False)
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id':'email_std',
        'class': 'form-control',
        'placeholder': 'Email'
    }),required=False)
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'id':'image-std',
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
        fields =  '__all__'


class StudentListForm(forms.ModelForm):
    className =forms.ModelChoiceField(queryset=Classes.objects.all(),widget=forms.Select({
        'id':'className_stdlist',
        'class': ' form-control',
        'placeholder': 'student-list',
         
        }),required=False)
    
    periods =forms.ModelChoiceField(queryset=Period.objects.all(),widget=forms.Select({
        'id':'periods_stdlist',
        'class': ' form-control',
        'placeholder': 'student-list',
         
        }),required=False)
    
    
    
    student = forms.ModelChoiceField(queryset=Student.objects.all(),widget=forms.Select({
        'id':'student_stdlist',
        'class': ' form-control',
        'placeholder': 'student-list',
         
        }),required=False)
    session = forms.ModelChoiceField(queryset=Session.objects.all(),widget=forms.Select({
        'id':'session_stdlist',
        'class': ' form-control',
        'placeholder': 'sezon_list',
         
        }),required=False)
    class Meta:
        model = StudentList
        fields =  '__all__'

class ParentForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'id':'firstName_stdp',
        'class': 'form-control',
        'placeholder': 'Adınız',
    }),required=False)
    
    lastName = forms.CharField(widget=forms.TextInput(attrs={
        'id':'lastName_stdp',
        'class': 'form-control',
        'placeholder': 'Adınız',
    }),required=False)
    
    student = forms.ModelChoiceField(queryset=Student.objects.all(),widget=forms.Select({
        'id':'student_stdp',
        'class': ' form-control',
        'placeholder': 'ogrenci',
         
        }),required=False)
    
    
    relation = forms.CharField(widget=forms.TextInput(attrs={
        'id':'relation_stdp',
        'class': 'form-control',
        'placeholder': 'Yakınlık Durumu',
        }),required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'id':'phone_stdp',
        'class': 'form-control',
        'placeholder': 'Telefon No'
    }),required=False)

    adsreds = forms.CharField(widget=forms.Textarea(attrs={
        'id':'address_stdp',
        'rows':'3' ,
        'cols':'30' ,
        'class': 'form-control',
        'placeholder': 'Adres',
        
    }),required=False)
    job = forms.CharField(widget=forms.TextInput(attrs={
        'id':'job_stdp',
        'class': 'form-control',
        'placeholder': 'İş Durumu'
    }),required=False)
    class Meta:
        model = Parent
        fields =  '__all__'
