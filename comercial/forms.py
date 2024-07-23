from django import forms
from .models import Setor, Estoque, AreaAcreditacao


class SetorForm(forms.ModelForm):
    # Defina as opções predefinidas para o campo 'tipo'
    TIPO_CHOICES = [
        ("LAB", "Laboratório"),
        ("ADM", "Administrativo"),
        ("FIN", "Financeiro"),
        ("RECEB", "Recebimento"),
        ("EXP", "Expedição"),
        ("MAN", "Manutenção"),
        ("RECEP", "Recepção"),
    ]

    # Defina o campo 'tipo' como um ChoiceField
    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES,
        label="Tipo",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    setor_destino = forms.ChoiceField(
        choices=TIPO_CHOICES,
        label="Setor Destino",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    estoque = forms.ModelChoiceField(
        queryset=Estoque.objects.all(),
        empty_label=None,
        label="Estoque",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Setor
        fields = "__all__"
        exclude = ["temperatura", "umidade", "pressao"]
        labels = {
            "nome": "Nome",
            "tipo": "Tipo",
            "sigla": "Sigla",
            "setor_destino": "Setor Destino",
            "estoque": "Estoque",
            "tempo_atividade": "Tempo de Atividade",
            "observacoes": "Observações",
            "temperatura": "Temperatura",
            "umidade": "Umidade",
            "pressao": "Pressão",
            "fa_registro": "FA Registro",
            "utilizado_fluxo": "Utilizado Fluxo",
            "bloquear_certificado_ko": "Bloquear Certificado KO",
        }

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "sigla": forms.TextInput(attrs={"class": "form-control"}),
            "tempo_atividade": forms.TextInput(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 1}),
            "temperatura": forms.TextInput(attrs={"class": "form-control"}),
            "umidade": forms.TextInput(attrs={"class": "form-control"}),
            "pressao": forms.TextInput(attrs={"class": "form-control"}), 
        }


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = "__all__"
        labels = {
            "nome": "Nome",
            "descricao": "Descrição",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
        }


class AcreditacaoForm(forms.ModelForm):
    class Meta:
        model = AreaAcreditacao
        fields = "__all__"
        labels = {
            "nome": "Nome",
            "descricao": "Descrição",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
        }
