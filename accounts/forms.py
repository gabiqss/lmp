# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from .models import CustomUser, AnexosColaborador
from multiupload.fields import MultiFileField


class CustomUserCreationForm(UserCreationForm):
    #anexos = MultiFileField(min_num=1, max_num=5, max_file_size=1024 * 1024 * 5)
    """
    Formulário de criação de usuário personalizado.

    Este formulário é usado para criar novos usuários no sistema.
    Ele estende o formulário padrão de criação de usuário do Django
    e adiciona campos personalizados conforme definido no modelo CustomUser.

    Attributes:
        anexos (MultiFileField): Campo para fazer upload de vários arquivos anexos.
    """
    # English
    """
    Form for creating a custom user.

    This form is used to create new users in the system.
    It extends the default Django user creation form
    and adds custom fields as defined in the CustomUser model.

    Attributes:
        anexos (MultiFileField): Field for uploading multiple attachment files.
    """
    class Meta:
        model = CustomUser
        fields = 'full_name', 'sexo', 'cep', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'celular', 'rg', 'cpf', 'habilitacao', 'pis', 'cargo', 'setor', 'data_admissao', 'data_desligamento', 'remuneracao', 'vale_transporte', 'nome_conjuge', 'rg_conjuge', 'cpf_conjuge', 'celular_conjuge', 'username', 'email', 'date_of_birth', 'is_active', 'is_superuser', 'password1', 'password2', 'foto'
        labels = {
            'full_name': 'Nome Completo',
            'sexo': 'Sexo',
            'cep': 'CEP',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'celular': 'Celular',
            'rg': 'RG',
            'cpf': 'CPF',
            'habilitacao': 'Habilitação',
            'pis': 'PIS',
            'cargo': 'Cargo',
            'setor': 'Setor',
            'data_admissao': 'Data de Admissão',
            'data_desligamento': 'Data de Desligamento',
            'remuneracao': 'Remuneração',
            'vale_transporte': 'Vale Transporte',
            'nome_conjuge': 'Nome do Cônjuge',
            'rg_conjuge': 'RG do Cônjuge',
            'cpf_conjuge': 'CPF do Cônjuge',
            'celular_conjuge': 'Celular do Cônjuge',
            'username': 'Nome de Usuário',
            'email': 'E-mail',
            'date_of_birth': 'Data de Nascimento',
            'is_active': 'Acessa o sistema',
            'is_superuser': 'Administrador',
            'anexos': 'Anexos',
            'foto': 'Foto',
            'password1': 'Senha',
            'password2': 'Confirme a Senha',
        }
        widgets = {
            'date_of_birth' : DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_admissao' : DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_desligamento' : DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "cep": forms.TextInput(attrs={"class": "form-control cep-input"}),
            "celular": forms.TextInput(attrs={"class": "form-control tel-input"}),
            "celular_conjuge": forms.TextInput(attrs={"class": "form-control tel-input"}),
            "cpf": forms.TextInput(attrs={"class": "form-control cpf-input"}),
            "cpf_conjuge": forms.TextInput(attrs={"class": "form-control cpf-input"}),
            "rg": forms.TextInput(attrs={"class": "form-control"}),
            "rg_conjuge": forms.TextInput(attrs={"class": "form-control"}),
            "pis": forms.TextInput(attrs={"class": "form-control"}),
            "habilitacao": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "estado": forms.TextInput(attrs={"class": "form-control"}),
            "cargo": forms.TextInput(attrs={"class": "form-control"}),
            "setor": forms.TextInput(attrs={"class": "form-control"}),
            "complemento": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "remuneracao": forms.TextInput(attrs={"class": "form-control"}),
            "vale_transporte": forms.TextInput(attrs={"class": "form-control"}),
            "nome_conjuge": forms.TextInput(attrs={"class": "form-control"}),
            "celular_conjuge": forms.TextInput(attrs={"class": "form-control"}),
            "anexos": MultiFileField(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "is_superuser": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        
class CustomUserEditionForm(UserCreationForm):
    #anexos = MultiFileField(min_num=1, max_num=5, max_file_size=1024 * 1024 * 5)
    """
    Formulário de edição de usuário personalizado.

    Este formulário é usado para editar informações de usuários existentes no sistema.
    Ele estende o formulário padrão de edição de usuário do Django
    e inclui campos personalizados conforme definido no modelo CustomUser.

    Attributes:
        anexos (MultiFileField): Campo para fazer upload de vários arquivos anexos.
        password (forms.PasswordInput): Campo para inserção da senha do usuário.
    """
    # English
    """
    Form for editing a custom user.

    This form is used to edit information of existing users in the system.
    It extends the default Django user edition form
    and includes custom fields as defined in the CustomUser model.

    Attributes:
        anexos (MultiFileField): Field for uploading multiple attachment files.
        password (forms.PasswordInput): Field for entering the user's password.
    """
    class Meta:
        model = CustomUser
        fields = 'full_name', 'sexo', 'cep', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'celular', 'rg', 'cpf', 'habilitacao', 'pis', 'cargo', 'setor', 'data_admissao', 'data_desligamento', 'remuneracao', 'vale_transporte', 'nome_conjuge', 'rg_conjuge', 'cpf_conjuge', 'celular_conjuge', 'email', 'date_of_birth', 'is_active', 'is_superuser'
        labels = {
            'full_name': 'Nome Completo',
            'sexo': 'Sexo',
            'cep': 'CEP',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'celular': 'Celular',
            'rg': 'RG',
            'cpf': 'CPF',
            'habilitacao': 'Habilitação',
            'pis': 'PIS',
            'cargo': 'Cargo',
            'setor': 'Setor',
            'data_admissao': 'Data de Admissão',
            'data_desligamento': 'Data de Desligamento',
            'remuneracao': 'Remuneração',
            'vale_transporte': 'Vale Transporte',
            'nome_conjuge': 'Nome do Cônjuge',
            'rg_conjuge': 'RG do Cônjuge',
            'cpf_conjuge': 'CPF do Cônjuge',
            'celular_conjuge': 'Celular do Cônjuge',
            'username': 'Nome de Usuário',
            'email': 'E-mail',
            'date_of_birth': 'Data de Nascimento',
            'is_active': 'Acessa o sistema',
            'is_superuser': 'Administrador',
            'anexos': 'Anexos',
            'foto': 'Foto',
            'password1': 'Senha',
            'password2': 'Confirme a Senha',
        }
        widgets = {
            'date_of_birth' : DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_admissao' : DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_desligamento' : DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "cep": forms.TextInput(attrs={"class": "form-control cep-input"}),
            "celular": forms.TextInput(attrs={"class": "form-control tel-input"}),
            "celular_conjuge": forms.TextInput(attrs={"class": "form-control tel-input"}),
            "cpf": forms.TextInput(attrs={"class": "form-control cpf-input"}),
            "cpf_conjuge": forms.TextInput(attrs={"class": "form-control cpf-input"}),
            "rg": forms.TextInput(attrs={"class": "form-control"}),
            "rg_conjuge": forms.TextInput(attrs={"class": "form-control"}),
            "pis": forms.TextInput(attrs={"class": "form-control"}),
            "habilitacao": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "estado": forms.TextInput(attrs={"class": "form-control"}),
            "cargo": forms.TextInput(attrs={"class": "form-control"}),
            "setor": forms.TextInput(attrs={"class": "form-control"}),
            "complemento": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "remuneracao": forms.TextInput(attrs={"class": "form-control"}),
            "vale_transporte": forms.TextInput(attrs={"class": "form-control"}),
            "nome_conjuge": forms.TextInput(attrs={"class": "form-control"}),
            "celular_conjuge": forms.TextInput(attrs={"class": "form-control"}),
            "anexos": MultiFileField(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "is_superuser": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class AnexosColaboradorForm(forms.ModelForm):
    class Meta:
        model = AnexosColaborador
        fields = ["anexo"]
        labels = {
            "anexo": "Anexo*",
        }
        widget = {
            "anexo": forms.FileInput(attrs={"class": "form-control"}),
        }