from django import forms

# Modelos
from .models import  Contact

class ContacForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('__all__')