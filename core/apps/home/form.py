from django import forms

from .models import ProfilDetay


class ProfilDetayForm(forms.ModelForm):

    class Meta:
        model = ProfilDetay
        fields = ('__all__')