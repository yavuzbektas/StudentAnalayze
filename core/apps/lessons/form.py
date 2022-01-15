

from unicodedata import name
from django import forms

from apps.home.models import Period, Session
from apps.lessons.models import Lesson, LessonClassList
from apps.student.models import Student, StudentList




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
    
    lessons = forms.ModelMultipleChoiceField(queryset=Lesson.objects.all(),widget=forms.Select({
        'id':'lessons',
        'class': ' form-control',
        'placeholder': 'lessons',
         
        }),required=False)
    className  = forms.ModelMultipleChoiceField(queryset=StudentList.objects.all(),widget=forms.Select({
        'id':'className',
        'class': ' form-control',
        'placeholder': 'className',
         
        }),required=False)
    """periods =forms.ModelChoiceField(queryset=Period.objects.all(),widget=forms.Select({
        'id':'periods_stdlist',
        'class': ' form-control',
        'placeholder': 'student-list',
         
        }),required=False)"""
    class Meta:
        model = LessonClassList
        fields =  "__all__"

    