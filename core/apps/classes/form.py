
from django import forms
from apps.home.models import Session,Period,Profil
from apps.classes.models import  Classes,ClassLevels,ClassNames
from apps.student.models import Student,StudentList,Parent,MiddleSchool,Period
from django.contrib.admin.widgets import AdminDateWidget




class ClassListForm(forms.ModelForm):
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