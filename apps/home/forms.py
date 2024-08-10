from django import forms
from .models import Menssage


class MeessageFromForm(forms.ModelForm):
    
    class Meta:
        model = Menssage
        fields = ("__al__",)
