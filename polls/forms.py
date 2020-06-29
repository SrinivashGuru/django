from django import forms
from .models import *

sex_types = (('Male', 'M'), ('Female', 'F'))

class my_class_form(forms.ModelForm):
    sex = forms.ChoiceField(choices=sex_types)
    class Meta:
        model = details
        fields = ['name', 'sex', 'age']