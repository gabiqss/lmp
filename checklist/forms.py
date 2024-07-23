from django import forms
from .models import Checklist

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['title'] 
        labels = {'title': 'Título'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'})}
