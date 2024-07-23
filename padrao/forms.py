from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib import messages


class GrandezaForm(ModelForm):
    class Meta:
        model = Grandeza
        fields = "__all__"
        labels = {
            "nome": "Nome",
            "descricao": "Descrição",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
        }


class Unidade_MedidaForm(ModelForm):
    class Meta:
        model = Unidade_Medida
        fields = "__all__"
        labels = {
            "nome": "Nome",
            "simbolo": "Símbolo",
            "grandeza": "Grandeza",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "simbolo": forms.TextInput(attrs={"class": "form-control"}),
            "grandeza": forms.Select(attrs={"class": "form-control"}),
        }


class ResolucaoForm(forms.ModelForm):
    class Meta:
        model = Resolucao
        fields = ["valor"]
        labels = {
            "valor": "Valor",
        }
        widgets = {
            "valor": forms.NumberInput(
                attrs={
                    "step": "0.0000000001",
                    "type": "number",
                    "class": "form-control",
                }
            ),
        }


class Tipo_PadrãoForm(ModelForm):
    class Meta:
        model = Tipo_Padrão
        fields = "__all__"
        labels = {
            "nome": "Nome",
            "observacao": "Observação",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "observacao": forms.Textarea(attrs={"class": "form-control"}),
        }


class FaixasForm(ModelForm):
    class Meta:
        model = Faixas
        fields = "__all__"
        labels = {
            "descricao": "Descrição",
            "unidade_medida": "Unidade de Medida",
            "amplitude_max": "Amplitude Máxima",
            "amplitude_min": "Amplitude Mínima",
            "resolucao": "Resolução",
        }
        widgets = {
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "unidade_medida": forms.Select(attrs={"class": "form-control"}),
            "amplitude_max": forms.NumberInput(attrs={"class": "form-control"}),
            "amplitude_min": forms.NumberInput(attrs={"class": "form-control"}),
            "resolucao": forms.Select(attrs={"class": "form-control"}),
        }


class Novo_PadrãoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Pega o request e remove do kwargs
        super().__init__(*args, **kwargs)
        
    prox_calibracao = forms.DateField(
        widget=forms.TextInput(attrs={"type": "date", "class": "form-control"})
    )
    prox_verificacao = forms.DateField(
        widget=forms.TextInput(attrs={"type": "date", "class": "form-control"})
    )
    faixas = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        queryset=Faixas.objects.all(),
        to_field_name="id"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        tipo_instrumento = cleaned_data.get('tipo_instrumento')

        # Verifique se já existe um padrão com o mesmo tipo de instrumento
        if tipo_instrumento:
            padrão_existente = Novo_Padrão.objects.filter(tipo_instrumento=tipo_instrumento).exists()
            if padrão_existente:
                messages.error(self.request, "Já existe um padrão com este tipo de instrumento.")
                print("Já existe um padrão com este tipo de instrumento.")
                raise forms.ValidationError("Já existe um padrão com este tipo de instrumento.")
                

        return cleaned_data

    class Meta:
        model = Novo_Padrão
        fields = "__all__"
        labels = {
            "tag": "TAG",
            "numero_serie": "Número de Série",
            "tipo_instrumento": "Tipo de Instrumento",
            "modelo_instrumento": "Modelo de Instrumento",
            "fabricante": "Fabricante",
            "setor_cliente": "Setor do Cliente",
            "prox_calibracao": "Próxima Calibração",
            "prox_verificacao": "Próxima Verificação",
            "calibrar a cada": "Calibrar a cada",
            "verificar a cada": "Verificar a cada",
            "padrao_status": "Status",
            "utilizado_campo": "Utilizado em Campo",
            "observacoes": "Observações",
            "calibrar_com": "Calibrar com",
            "faixas": "Faixas",
        }
        widgets = {
            "tag": forms.TextInput(attrs={"class": "form-control"}),
            "numero_serie": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_instrumento": forms.Select(attrs={"class": "form-control"}),
            "modelo_instrumento": forms.Select(attrs={"class": "form-control"}),
            "fabricante": forms.Select(attrs={"class": "form-control"}),
            "setor_cliente": forms.TextInput(attrs={"class": "form-control"}),
            "prox_calibracao": forms.TextInput(attrs={"class": "form-control"}),
            "prox_verificacao": forms.TextInput(attrs={"class": "form-control"}),
            "calibrar_a_cada": forms.TextInput(attrs={"class": "form-control"}),
            "verificar_a_cada": forms.TextInput(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control"}),
            "calibrar_com": forms.Select(attrs={"class": "form-control"}),
            "faixas" : forms.Select(attrs={"class": "form-control"}),
    
        }


class Criterio_AceitacaoForm(ModelForm):
    class Meta:
        model = Criterio_Aceitacao
        fields = "__all__"
        labels = {
            "nome": "Nome",
            "formula_de_validacao": "Fórmula de Validação",
            "grandeza": "Grandeza",
            "unidade_medida": "Unidade de Medida",
            "amplitude_max": "Amplitude Máxima",
            "amplitude_min": "Amplitude Mínima",
            "limite_max": "Limite Máximo",
            "limite_min": "Limite Mínimo",
            "padrao_id": "ID Padrão",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "formula_de_validacao": forms.Select(attrs={"class": "form-control"}),
            "grandeza": forms.Select(attrs={"class": "form-control"}),
            "unidade_medida": forms.Select(attrs={"class": "form-control"}),
            "amplitude_max": forms.NumberInput(attrs={"class": "form-control"}),
            "amplitude_min": forms.NumberInput(attrs={"class": "form-control"}),
            "limite_max": forms.NumberInput(attrs={"class": "form-control"}),
            "limite_min": forms.NumberInput(attrs={"class": "form-control"}),
            "padrao_id": forms.Select(attrs={"class": "form-control"}),
        }
