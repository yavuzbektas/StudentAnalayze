from django import forms


from apps.polls.models import Kullanicilar





class testForm(forms.ModelForm):


    class Meta:
        model=Kullanicilar
        fields=['ad',]