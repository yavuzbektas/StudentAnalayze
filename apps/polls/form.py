from django import forms


from apps.polls.models import Kullanicilar
import apps.polls.models 




class testForm(forms.ModelForm):



    class Meta:
        model=Kullanicilar
        fields=['ad','TC']

        class Meta:
         model=apps.polls.models.Kullanicilar
         fields=['ad',]

