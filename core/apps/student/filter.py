import django_filters
from .models import Student
from django import forms
class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['image','birtdate']

