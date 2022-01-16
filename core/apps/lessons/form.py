

from unicodedata import name
from django import forms

from apps.home.models import Period, Session
from apps.lessons.models import Lesson, LessonClassList
from apps.student.models import Student, StudentList
from apps.home.models import Profil

class MyModelChoiceField_lesson(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.className
class MyModelChoiceField_teacher(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.className
class MyModelChoiceField_class(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.className
    
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
        'id':'lesson_teacherID',
        'class': ' form-control',
        'placeholder': 'Ders Öğretmeni',
         
        }),required=False)
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all(),widget=forms.Select({
        'id':'lesson_lessonID',
        'class': ' form-control',
        'placeholder': 'Ders',
         
        }),required=False)
    className  = MyModelChoiceField_class(queryset=StudentList.objects.all(),widget=forms.Select({
        'id':'lesson_classnameID',
        'class': ' form-control',
        'placeholder': 'Sınıf', 
        }),required=False)
    
    class Meta:
        model = LessonClassList
        fields =  "__all__"

    