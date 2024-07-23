from django.forms import ModelForm
from django import forms
from .models import Procedimento_eletronico, ValoresCalculos


class ProcElet_Form(ModelForm):
    ult_analise_critica = forms.DateField(
        widget=forms.TextInput(attrs={"type": "date", "class": "form-control"}),
        label="Última Análise Crítica"
    )

    class Meta:
        model = Procedimento_eletronico
        fields = "__all__"
        labels = {
            "tipo_procedimento": "Tipo de Procedimento",
            "codigo": "Código",
            "nome": "Nome",
            "cliente": "Cliente",
            "tipo_instrumento": "Tipo de Instrumento",
            "tipo_calibracao": "Tipo de Calibração",
            "local": "Local", 
            "periodo_revisao": "Período de Revisão",
            "observacoes": "Observações",
        }
        widgets = {
            "tipo_procedimento": forms.Select(attrs={"class": "form-control"}),
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "tipo_instrumento": forms.Select(attrs={"class": "form-control"}),
            "tipo_calibracao": forms.Select(attrs={"class": "form-control"}),
            "local": forms.Select(attrs={"class": "form-control"}),
            "periodo_revisao": forms.NumberInput(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class ValoresCalculos_Form(ModelForm):
    class Meta:
        model = ValoresCalculos
        fields = "__all__"
        widgets = {
            "procedimento": forms.Select(attrs={"class": "form-control"}),
        }
