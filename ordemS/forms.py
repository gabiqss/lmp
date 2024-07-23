from django import forms
from django.forms import DateInput

from .models import Dados, OrdemDeServico


class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados
        exclude = ("data_cadastro", "status", "contato")
        labels = {
            "razao_social": "Razão Social",
            "cnpj": "CNPJ",
            "cep": "CEP",
            "endereco": "Endereço",
            "cidade": "Cidade",
            "bairro": "Bairro",
            "fone": "Telefone",
            "fax": "Fax",
            "contrato": "Contrato",
            "nota_fiscal": "Nota Fiscal",
            "tipo_envio": "Tipo de Envio",
            "embalagem": "Embalagem",
            "data_chamado": "Data do Chamado",
            "data_atendimento": "Data do Atendimento",
            "data_entrada": "Data de Entrada",
            "saida_prevista": "Saída Prevista",
            "info_instrumentos": "Informações dos Instrumentos",
            "arquivo_pdf": "Arquivo PDF",
            "observacoes": "Observações",
            "setor": "Setor",
        }
        widgets = {
            "razao_social": forms.TextInput(attrs={"class": "form-control"}),
            "cnpj": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(attrs={"class": "form-control"}),
            "endereco": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
            "fone": forms.TextInput(attrs={"class": "form-control"}),
            "fax": forms.TextInput(attrs={"class": "form-control"}),
            "contrato": forms.TextInput(attrs={"class": "form-control"}),
            "nota_fiscal": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_envio": forms.TextInput(attrs={"class": "form-control"}),
            "embalagem": forms.TextInput(attrs={"class": "form-control"}),
            "data_chamado": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "data_atendimento": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "data_entrada": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "saida_prevista": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "info_instrumentos": forms.Textarea(
                attrs={"class": "form-control", "rows": 1}
            ),
            "arquivo_pdf": forms.FileInput(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 1}),
            "setor": forms.Select(attrs={"class": "form-control"}),
        }

class DadosFormEdit(forms.ModelForm):
    class Meta:
        model = Dados
        exclude = ("data_cadastro",)  # Note a vírgula após o campo
        labels = {
            "razao_social": "Razão Social",
            "cnpj": "CNPJ",
            "cep": "CEP",
            "endereco": "Endereço",
            "cidade": "Cidade",
            "bairro": "Bairro",
            "fone": "Telefone",
            "fax": "Fax",
            "contrato": "Contrato",
            "nota_fiscal": "Nota Fiscal",
            "tipo_envio": "Tipo de Envio",
            "embalagem": "Embalagem",
            "data_chamado": "Data do Chamado",
            "data_atendimento": "Data do Atendimento",
            "data_entrada": "Data de Entrada",
            "saida_prevista": "Saída Prevista",
            "info_instrumentos": "Informações dos Instrumentos",
            "arquivo_pdf": "Arquivo PDF",
            "observacoes": "Observações",
            "setor": "Setor",
            "status": "Status",
            "contato": "Contato",
        }
        widgets = {
            "razao_social": forms.TextInput(
                attrs={"class": "form-control", "readonly": True}
            ),
            "cnpj": forms.TextInput(attrs={"class": "form-control", "readonly": True}),
            "cep": forms.TextInput(attrs={"class": "form-control"}),
            "endereco": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
            "fone": forms.TextInput(attrs={"class": "form-control"}),
            "fax": forms.TextInput(attrs={"class": "form-control"}),
            "contrato": forms.TextInput(attrs={"class": "form-control"}),
            "nota_fiscal": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_envio": forms.TextInput(attrs={"class": "form-control"}),
            "embalagem": forms.TextInput(attrs={"class": "form-control"}),
            "data_chamado": forms.TextInput(
                attrs={"type": "date", "class": "form-control", "readonly": True}
            ),
            "data_atendimento": forms.TextInput(
                attrs={"type": "date", "class": "form-control", "readonly": True}
            ),
            "data_entrada": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "saida_prevista": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "info_instrumentos": forms.Textarea(
                attrs={"class": "form-control", "rows": 1}
            ),
            "arquivo_pdf": forms.FileInput(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 1}),
            "setor": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "contato": forms.TextInput(attrs={"class": "form-control"}),
        }
