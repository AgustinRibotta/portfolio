from django import forms
from .models import Menssage


class MeessageForm(forms.ModelForm):
    
    class Meta:
        model = Menssage
        fields = ['name', 'email', 'menssage']
