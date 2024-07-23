from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import InstrumentsInstruments, InstrumentTypes, InstrumentsModels
from comercial.models import *
from procedimentos.models import Dados_procedimento


class CadastroInstruments(ModelForm):
    is_active = forms.BooleanField(label="Instrumento ativo", required=False)

    class Meta:
        model = InstrumentsInstruments
        fields = (
            "code",
            "serial_number",
            "tag",
            "next_calibration",
            "description",
            "calibration_frequency_months",
            "is_active",
        )
        labels = {
            "code": "Código",
            "serial_number": "Número de série",
            "tag": "TAG",
            "next_calibration": "Próxima calibração",
            "description": "Descrição",
            "calibration_frequency_months": "Frequência de calibração (meses)",
            "is_active": "Instrumento ativo",
        }
        widgets = {
            "next_calibration": DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "code": forms.TextInput(attrs={"class": "form-control"}),
            "serial_number": forms.TextInput(attrs={"class": "form-control"}),
            "tag": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "calibration_frequency_months": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class InstrumentTypeForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Nome', max_length=100)
    procedimento = forms.ModelMultipleChoiceField(
        queryset=Dados_procedimento.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),   
    )
    setor = forms.ModelChoiceField(
        queryset=Setor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    area_acreditaco = forms.ModelChoiceField(
        queryset=AreaAcreditacao.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'label': 'Área de Acreditação'}),
        label='Área de Acreditação'
    )
    condicoes_ambientais_umi = forms.DecimalField(max_digits=7, decimal_places=2, label='Condições Ambientais (Umidade)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    condicoes_ambientais_temp = forms.DecimalField(max_digits=7, decimal_places=2, label='Condições Ambientais (Temperatura)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    condicoes_ambientais_pre = forms.DecimalField(max_digits=7, decimal_places=2, label='Condições Ambientais (Pressão)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    observacao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Observação', required=False)
    
    class Meta:
        model = InstrumentTypes
        fields = "__all__"

    faixas_padronizadas = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label='Faixas Padronizadas', required=False)


class InstrumentsModelsForm(forms.ModelForm):
    class Meta:
        model = InstrumentsModels
        fields = "__all__"
        labels = {
            "name": "Nome",
            "instrument_type": "Tipo de instrumento",
            "description": "Descrição",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "instrument_type": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 1}),
        }
