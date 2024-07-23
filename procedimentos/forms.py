from django import forms
from .models import Dados_procedimento, ArquivoPDF

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Dados_procedimento
        fields = ['codigo', 'titulo', 'descricao']
        labels = {
            'codigo': 'Código',
            'titulo': 'Título',
            'descricao': 'Descrição',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ArquivoPDFForm(forms.ModelForm):
    class Meta:
        model = ArquivoPDF
        fields = ['arquivo']
        labels = {
            'arquivo': 'Arquivo',
        }
        widgets = {
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }
