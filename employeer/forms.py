from django import forms

from .models import Employeer

class EmployeerForm(forms.ModelForm):
    class Meta:
        model = Employeer
        fields = '__all__'
        