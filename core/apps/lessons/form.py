

from unicodedata import name
from django import forms

from apps.home.models import Period, Session
from apps.lessons.models import Lesson, LessonClassList
from apps.student.models import Student, StudentList
from apps.home.models import Profil



class lessonForm(forms.ModelForm):
    name  = forms.CharField(widget=forms.TextInput(attrs={
        'id':'name',
        'class': 'form-control',
        'placeholder': 'name',
    }),required=False)
    code  = forms.CharField(widget=forms.TextInput(attrs={
        'id':'code',
        'class': 'form-control',
        'placeholder': 'code',
    }),required=False)
    class Meta:
        model = Lesson
        fields =  "__all__"


class LessonClassListForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Profil.objects.all(),widget=forms.Select({
        'id':'lesson_teacher',
        'class': ' form-control',
        'placeholder': 'Ders Öğretmeni',
         
        }),required=False)
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all(),widget=forms.Select({
        'id':'lessons',
        'class': ' form-control',
        'placeholder': 'Ders',
         
        }),required=False)
    className  = forms.ModelChoiceField(queryset=StudentList.objects.all(),widget=forms.Select({
        'id':'className',
        'class': ' form-control',
        'placeholder': 'Sınıf',
         
        }),required=False)
    
    class Meta:
        model = LessonClassList
        fields =  "__all__"

    