from django import forms
from django.forms import ModelForm
from .models import Customers_main, Contacts_Customers, AnexosCliente, Fornecedores
from django.forms.models import inlineformset_factory
from pycpfcnpj import cpfcnpj

# Forms de cadastro de clientes CNPJ


class Cadatrar_Clientes(ModelForm):
    """
    Form for registering customers with CNPJ.
    """
    OPCOES_TAMANHO = [('pequeno', 'Pequeno'),('medio', 'Médio'),('grande', 'Grande')]
    class Meta:
        model = Customers_main
        fields = (
            "cnpj",
            "name",
            "phone",
            "email",
            "corporate_name",
            "municipal_registration",
            "state_registration",
            "address",
            "city",
            "uf",
            "cep",
            "fax",
            "neighborhood",
            "date_of_fundation",
            "web_site",
            "id_market_segment",
            "id_size",
            "address_number",
            "address_complement",
            "payment_day",
            "is_requestor_in_field",
            "payment_venc",
            "company_responsible",
            "credit_or_debit_card",
            "description",
            "tipo_cliente"
        )
        labels = {
            "cnpj": "CNPJ*",
            "name": "Nome*",
            "phone": "Telefone*",
            "email": "E-mail*",
            "corporate_name": "Razão Social*",
            "municipal_registration": "Inscrição Municipal",
            "state_registration": "Inscrição Estadual",
            "address": "Endereço*",
            "city": "Cidade*",
            "uf": "UF*",
            "cep": "CEP*",
            "fax": "Fax",
            "neighborhood": "Bairro*",
            "date_of_fundation": "Data de Fundação",
            "web_site": "Site",
            "id_market_segment": "Segmento de Mercado",
            "id_size": "Porte",
            "address_number": "Número*",
            "address_complement": "Complemento",
            "payment_day": "Dia de Pagamento",
            "is_requestor_in_field": "Solicitante em Campo",
            "payment_venc": "Vencimento",
            "company_responsible": "Empresa Responsável",
            "credit_or_debit_card": "Cartão de Crédito ou Débito",
            "description": "Descrição",
            "tipo_cliente": "Tipo do cliente*",
        }
        widgets = {
            "payment_day": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "payment_venc": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "cnpj": forms.TextInput(attrs={"class": "form-control cnpj-input "}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control tel-input"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "corporate_name": forms.TextInput(attrs={"class": "form-control"}),
            "municipal_registration": forms.TextInput(attrs={"class": "form-control"}),
            "state_registration": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control "}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "uf": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(attrs={"class": "form-control cep-input"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "fax": forms.TextInput(attrs={"class": "form-control"}),
            "neighborhood": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_fundation": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "web_site": forms.TextInput(attrs={"class": "form-control"}),
            "id_market_segment": forms.TextInput(attrs={"class": "form-control"}),
            "id_size": forms.Select(choices=[
        ('pequeno porte', 'Pequeno porte'),
        ('medio porte', 'Médio porte'),
        ('grande porte', 'Grande porte'),
    ], attrs={"class":"form-control"}),
            "address_number": forms.TextInput(attrs={"class": "form-control"}),
            "address_complement": forms.TextInput(attrs={"class": "form-control"}),
            "is_requestor_in_field": forms.TextInput(attrs={"class": "form-control"}),
            "company_responsible": forms.TextInput(attrs={"class": "form-control"}),
            "credit_or_debit_card": forms.Select(attrs={"class": "form-control"}),
            "tipo_cliente": forms.Select(attrs={"class": "form-control"}),
        }
    def clean_cnpj(self):
        """
        Validate CNPJ field and check for duplicate entries.
        """

        instance = self.instance
        cnpj_numero = self.cleaned_data["cnpj"]
        if not cpfcnpj.validate(cnpj_numero):
            raise forms.ValidationError("CNPJ inválido")
        if not instance:
            existing_contato = Customers_main.objects.filter(cnpj=cnpj_numero).exists()
        else:
            existing_contato = Customers_main.objects.filter(
                cnpj=cnpj_numero
            ).exclude(pk=instance.pk).exists()
        if existing_contato:
            raise forms.ValidationError("CNPJ já cadastrado")

        return cnpj_numero
    
# Forms de cadastro de clientes


class Cadatrar_Clientes_CPF(ModelForm):
    """
    Form for registering customers with CPF.
    """

    class Meta:
        model = Customers_main
        fields = (
            "name",
            "cpf",
            "phone",
            "email",
            "address",
            "city",
            "uf",
            "cep",
            "neighborhood",
            "address_number",
            "address_complement",
            "payment_day",
            "is_requestor_in_field",
            "payment_venc",
            "company_responsible",
            "credit_or_debit_card",
            "description",
            "tipo_cliente"
        )
        labels = {
            "name": "Nome*",
            "cpf": "CPF*",
            "phone": "Telefone*",
            "email": "E-mail*",
            "address": "Endereço*",
            "city": "Cidade*",
            "uf": "UF*",
            "cep": "CEP*",
            "neighborhood": "Bairro*",
            "address_number": "Número*",
            "address_complement": "Complemento",
            "payment_day": "Dia de Pagamento",
            "is_requestor_in_field": "Solicitante em Campo",
            "payment_venc": "Vencimento",
            "company_responsible": "Empresa Responsável",
            "credit_or_debit_card": "Cartão de Crédito ou Débito",
            "description": "Descrição",
            "tipo_cliente": "Tipo do cliente*",
        }
        widgets = {
            "payment_day": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "payment_venc": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "cpf": forms.TextInput(attrs={"class": "form-control cpf-input"}),
            "cnpj": forms.TextInput(attrs={"class": "form-control cnpj-input "}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control tel-input"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "corporate_name": forms.TextInput(attrs={"class": "form-control"}),
            "municipal_registration": forms.TextInput(attrs={"class": "form-control"}),
            "state_registration": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control "}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "uf": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(attrs={"class": "form-control cep-input"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "fax": forms.TextInput(attrs={"class": "form-control"}),
            "neighborhood": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_fundation": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "web_site": forms.TextInput(attrs={"class": "form-control"}),
            "id_market_segment": forms.TextInput(attrs={"class": "form-control"}),
            "id_size": forms.Select(choices=[
        ('pequeno porte', 'Pequeno porte'),
        ('medio porte', 'Médio porte'),
        ('grande porte', 'Grande porte'),
    ], attrs={"class":"form-control"}),
            "address_number": forms.TextInput(attrs={"class": "form-control"}),
            "address_complement": forms.TextInput(attrs={"class": "form-control"}),
            "is_requestor_in_field": forms.TextInput(attrs={"class": "form-control"}),
            "company_responsible": forms.TextInput(attrs={"class": "form-control"}),
            "credit_or_debit_card": forms.Select(attrs={"class": "form-control"}),
            "tipo_cliente": forms.Select(attrs={"class": "form-control"}),
        }
    
    
    def clean_cpf(self):
        """
        Validate CPF field and check for duplicate entries.
        """

        instance = self.instance
        cpf_numero = self.cleaned_data["cpf"] or '000.000.000-00'
        if cpf_numero != '000.000.000-00':
            if not cpfcnpj.validate(cpf_numero):
                raise forms.ValidationError("CPF inválido")
            if not instance:
                existing_contato = Contacts_Customers.objects.filter(cpf=cpf_numero).exists()
            else:
                existing_contato = Contacts_Customers.objects.filter(
                    cpf=cpf_numero
                ).exclude(pk=instance.pk).exists()
            if existing_contato:
                raise forms.ValidationError("CPF já cadastrado")
            return cpf_numero
        else:
            return cpf_numero

# Forms de contatos de clientes


class Contatos_Clientes(ModelForm):
    """
    Formulário para os contatos dos clientes.

    Campos:
        name (str): Nome do contato.
        cpf (str): CPF do contato.
        sector (str): Setor do contato.
        email (str): E-mail do contato.
        commercial_phone (str): Telefone comercial do contato.
        cellular (str): Celular do contato.
        description (str): Descrição do contato.

    Retorna:
        str: CPF válido.

    Raises:
        ValidationError: Se o CPF for inválido ou já estiver cadastrado.
    """
    # English
    """
    Form for customer contacts.

    Fields:
        name (str): Contact's name.
        cpf (str): Contact's CPF.
        sector (str): Contact's sector.
        email (str): Contact's email.
        commercial_phone (str): Contact's commercial phone number.
        cellular (str): Contact's cellular phone number.
        description (str): Contact's description.

    Returns:
        str: Valid CPF.

    Raises:
        ValidationError: If the CPF is invalid or already registered.
    """

    class Meta:
        model = Contacts_Customers
        fields = (
            "name",
            "cpf",
            "sector",
            "email",
            "commercial_phone",
            "cellular",
            "description",
        )
        labels = {
            "name": "Nome*",
            "cpf": "CPF",
            "sector": "Setor*",
            "email": "E-mail*",
            "commercial_phone": "Telefone Comercial",
            "cellular": "Celular",
            "description": "Descrição",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control cpf-input"}),
            "sector": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "commercial_phone": forms.TextInput(
                attrs={"class": "form-control tel-input"}
            ),
            "cellular": forms.TextInput(
                attrs={"class": "form-control phone-input phone-input"}
            ),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def clean_cpf(self):
        """
        Valida o campo CPF e verifica se já existe um cadastro com o mesmo número.
        """
        """
        Validates the CPF field and checks if there is already a registration with the same number.
        """

        instance = self.instance
        cpf_numero = self.cleaned_data["cpf"] or '000.000.000-00'
        if cpf_numero != '000.000.000-00':
            if not cpfcnpj.validate(cpf_numero):
                raise forms.ValidationError("CPF inválido")
            if not instance:
                existing_contato = Contacts_Customers.objects.filter(cpf=cpf_numero).exists()
            else:
                existing_contato = Contacts_Customers.objects.filter(
                    cpf=cpf_numero
                ).exclude(pk=instance.pk).exists()
            if existing_contato:
                raise forms.ValidationError("CPF já cadastrado")
            return cpf_numero
        else:
            return cpf_numero
        


PessoaContatoFormSet = inlineformset_factory(
    Customers_main, Contacts_Customers, form=Contatos_Clientes, extra=1
)


class EmpresaForm(forms.Form):
    """
    Form for registering customers with CNPJ.
    """

    cnpj = forms.CharField(
        label="CNPJ",
        max_length=18,
        widget=forms.TextInput(attrs={"class": "form-control cnpj-input"}),
        error_messages={
            "invalid": "CNPJ inválido",
            "already_exists": "CNPJ já cadastrado",
        },
    )

    def clean_cnpj(self):
        """
        Validate CNPJ field and check for duplicate entries.
        """
        
        cnpj = self.cleaned_data["cnpj"]
        cnpj = cnpj.replace(".", "").replace("-", "").replace("/", "").replace("_", "")

        if not cpfcnpj.validate(cnpj):
            raise forms.ValidationError(self.fields["cnpj"].error_messages["invalid"])

        if len(cnpj) != 14:
            raise forms.ValidationError(self.fields["cnpj"].error_messages["invalid"])

        if Customers_main.objects.filter(cnpj=cnpj).exists():
            raise forms.ValidationError(
                self.fields["cnpj"].error_messages["already_exists"]
            )

        return cnpj
    
class AnexosClienteForm(ModelForm):
    class Meta:
        model = AnexosCliente
        fields = ["anexo"]
        labels = {
            "anexo": "Anexo*",
        }
        widget = {
            "anexo": forms.FileInput(attrs={"class": "form-control"}),
        }

class Contatos_Clientes_select(ModelForm):
    """
    Formulário para os contatos dos clientes.

    Campos:
        name (str): Nome do contato.
        cpf (str): CPF do contato.
        sector (str): Setor do contato.
        email (str): E-mail do contato.
        commercial_phone (str): Telefone comercial do contato.
        cellular (str): Celular do contato.
        description (str): Descrição do contato.

    Retorna:
        str: CPF válido.

    Raises:
        ValidationError: Se o CPF for inválido ou já estiver cadastrado.
    """
    # English
    """
    Form for customer contacts.

    Fields:
        name (str): Contact's name.
        cpf (str): Contact's CPF.
        sector (str): Contact's sector.
        email (str): Contact's email.
        commercial_phone (str): Contact's commercial phone number.
        cellular (str): Contact's cellular phone number.
        description (str): Contact's description.

    Returns:
        str: Valid CPF.

    Raises:
        ValidationError: If the CPF is invalid or already registered.
    """
    id_customer = forms.ModelChoiceField(
        queryset=Customers_main.objects.all(), label="Cliente*", widget=forms.Select(attrs={'class': 'form-control select2'}), required=True
    )
    class Meta:
        model = Contacts_Customers
        fields = (
            "id_customer",
            "name",
            "cpf",
            "sector",
            "email",
            "commercial_phone",
            "cellular",
            "description",
            
        )
        labels = {
            "name": "Nome*",
            "cpf": "CPF",
            "sector": "Setor*",
            "email": "E-mail*",
            "commercial_phone": "Telefone Comercial",
            "cellular": "Celular",
            "description": "Descrição",
            
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control cpf-input"}),
            "sector": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "commercial_phone": forms.TextInput(
                attrs={"class": "form-control tel-input"}
            ),
            "cellular": forms.TextInput(
                attrs={"class": "form-control phone-input phone-input"}
            ),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

class FornecedoresForm(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = [
            "name", "cnpj", "phone", "email", "corporate_name",
            "municipal_registration", "state_registration", "address",
            "city", "uf", "cep", "description", "fax", "neighborhood",
            "date_of_fundation", "web_site", "id_market_segment",
            "id_size", "address_number", "address_complement", "payment_day",
            "is_requestor_in_field", "payment_venc", "company_responsible",
            "credit_or_debit_card", "tipo_cliente", "retorna_rapidamente",
            "data_retorna_rapidamente", "soluciona_problemas",
            "data_soluciona_problemas", "produto_fornecidos",
            "fornecedor_acreditado", "fornecedor_cnpj_ativo",
            "desempenha_qualidade", "custo_beneficio", "credibilidade"
        ]
        labels = {
            "name": "Nome*",
            "cnpj": "CNPJ",
            "cpf": "CPF",
            "phone": "Telefone",
            "email": "E-mail*",
            "corporate_name": "Razão Social",
            "municipal_registration": "Inscrição Municipal",
            "state_registration": "Inscrição Estadual",
            "address": "Endereço*",
            "city": "Cidade*",
            "uf": "UF*",
            "cep": "CEP*",
            "description": "Descrição",
            "fax": "Fax",
            "neighborhood": "Bairro*",
            "date_of_fundation": "Data de Fundação",
            "web_site": "Website",
            "id_market_segment": "Segmento de Mercado",
            "id_size": "Porte",
            "address_number": "Número",
            "address_complement": "Complemento",
            "payment_day": "Dia de Pagamento",
            "is_requestor_in_field": "Solicitante em campo",
            "payment_venc": "Vencimento do Pagamento",
            "company_responsible": "Responsável pela Empresa",
            "credit_or_debit_card": "Cartão de Crédito/Débito",
            "tipo_cliente": "Tipo de Cliente*",
            "retorna_rapidamente": "O prestador retorna os contatos rapidamente?",
            "data_retorna_rapidamente": "Data de avaliação de Retorno Rápido",
            "soluciona_problemas": "Soluciona os problemas rapidamente?",
            "data_soluciona_problemas": "Data de avaliação de Soluciona Rapidamente",
            "produto_fornecidos": "Produto/Serviço Fornecidos",
            "fornecedor_acreditado": "O fornecedor é acreditado?",
            "fornecedor_cnpj_ativo": "Fornecedor com CNPJ ativo?",
            "desempenha_qualidade": "Desempenha as atividades contratadas com qualidade?",
            "custo_beneficio": "Custo benefício e condições de pagamento",
            "credibilidade": "Credibilidade e experiência no mercado"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "cnpj": forms.TextInput(attrs={"class": "form-control cnpj-input"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "corporate_name": forms.TextInput(attrs={"class": "form-control"}),
            "municipal_registration": forms.TextInput(attrs={"class": "form-control"}),
            "state_registration": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "uf": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "fax": forms.TextInput(attrs={"class": "form-control"}),
            "neighborhood": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_fundation": forms.TextInput(attrs={"class": "form-control"}),
            "web_site": forms.TextInput(attrs={"class": "form-control"}),
            "id_market_segment": forms.TextInput(attrs={"class": "form-control"}),
            "id_size": forms.TextInput(attrs={"class": "form-control"}),
            "address_number": forms.TextInput(attrs={"class": "form-control"}),
            "address_complement": forms.TextInput(attrs={"class": "form-control"}),
            "payment_day": forms.TextInput(attrs={"class": "form-control"}),
            "is_requestor_in_field": forms.TextInput(attrs={"class": "form-control"}),
            "payment_venc": forms.TextInput(attrs={"class": "form-control"}),
            "company_responsible": forms.TextInput(attrs={"class": "form-control"}),
            "credit_or_debit_card": forms.Select(attrs={"class": "form-control"}),
            "tipo_cliente": forms.Select(attrs={"class": "form-control"}),
            "retorna_rapidamente": forms.Select(attrs={"class": "form-control"}),
            "data_retorna_rapidamente": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "soluciona_problemas": forms.Select(attrs={"class": "form-control"}),
            "data_soluciona_problemas": forms.TextInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "produto_fornecidos": forms.Select(attrs={"class": "form-control"}),
            "fornecedor_acreditado": forms.Select(attrs={"class": "form-control"}),
            "fornecedor_cnpj_ativo": forms.Select(attrs={"class": "form-control"}),
            "desempenha_qualidade": forms.Select(attrs={"class": "form-control"}),
            "custo_beneficio": forms.Select(attrs={"class": "form-control"}),
            "credibilidade": forms.Select(attrs={"class": "form-control"})
        }

class FornecedoresCPFForm(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = [
            "name", "cpf", "phone", "email", "address",
            "city", "uf", "cep", "description", "fax", "neighborhood",
            "address_number", "address_complement", "payment_day",
            "is_requestor_in_field", "payment_venc", "company_responsible",
            "credit_or_debit_card", "tipo_cliente", "retorna_rapidamente",
            "data_retorna_rapidamente", "soluciona_problemas",
            "data_soluciona_problemas", "produto_fornecidos",
            "fornecedor_acreditado", "fornecedor_cnpj_ativo",
            "desempenha_qualidade", "custo_beneficio", "credibilidade"
        ]
        labels = {
            "name": "Nome*",
            "cnpj": "CNPJ",
            "cpf": "CPF",
            "phone": "Telefone",
            "email": "E-mail*",
            "corporate_name": "Razão Social",
            "municipal_registration": "Inscrição Municipal",
            "state_registration": "Inscrição Estadual",
            "address": "Endereço*",
            "city": "Cidade*",
            "uf": "UF*",
            "cep": "CEP*",
            "description": "Descrição",
            "fax": "Fax",
            "neighborhood": "Bairro*",
            "date_of_fundation": "Data de Fundação",
            "web_site": "Website",
            "id_market_segment": "Segmento de Mercado",
            "id_size": "Porte",
            "address_number": "Número",
            "address_complement": "Complemento",
            "payment_day": "Dia de Pagamento",
            "is_requestor_in_field": "Solicitante em campo",
            "payment_venc": "Vencimento do Pagamento",
            "company_responsible": "Responsável pela Empresa",
            "credit_or_debit_card": "Cartão de Crédito/Débito",
            "tipo_cliente": "Tipo de Cliente*",
            "retorna_rapidamente": "O prestador retorna os contatos rapidamente?",
            "data_retorna_rapidamente": "Data de avaliação de Retorno Rápido",
            "soluciona_problemas": "Soluciona os problemas rapidamente?",
            "data_soluciona_problemas": "Data de avaliação de Soluciona Rapidamente",
            "produto_fornecidos": "Produto/Serviço Fornecidos",
            "fornecedor_acreditado": "O fornecedor é acreditado?",
            "fornecedor_cnpj_ativo": "Fornecedor com CNPJ ativo?",
            "desempenha_qualidade": "Desempenha as atividades contratadas com qualidade?",
            "custo_beneficio": "Custo benefício e condições de pagamento",
            "credibilidade": "Credibilidade e experiência no mercado"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "cnpj": forms.TextInput(attrs={"class": "form-control cnpj-input"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "corporate_name": forms.TextInput(attrs={"class": "form-control"}),
            "municipal_registration": forms.TextInput(attrs={"class": "form-control"}),
            "state_registration": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "uf": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "fax": forms.TextInput(attrs={"class": "form-control"}),
            "neighborhood": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_fundation": forms.TextInput(attrs={"class": "form-control"}),
            "web_site": forms.TextInput(attrs={"class": "form-control"}),
            "id_market_segment": forms.TextInput(attrs={"class": "form-control"}),
            "id_size": forms.TextInput(attrs={"class": "form-control"}),
            "address_number": forms.TextInput(attrs={"class": "form-control"}),
            "address_complement": forms.TextInput(attrs={"class": "form-control"}),
            "payment_day": forms.TextInput(attrs={"class": "form-control"}),
            "is_requestor_in_field": forms.TextInput(attrs={"class": "form-control"}),
            "payment_venc": forms.TextInput(attrs={"class": "form-control"}),
            "company_responsible": forms.TextInput(attrs={"class": "form-control"}),
            "credit_or_debit_card": forms.Select(attrs={"class": "form-control"}),
            "tipo_cliente": forms.Select(attrs={"class": "form-control"}),
            "retorna_rapidamente": forms.Select(attrs={"class": "form-control"}),
            "data_retorna_rapidamente": forms.DateInput(attrs={"class": "form-control"}),
            "soluciona_problemas": forms.Select(attrs={"class": "form-control"}),
            "data_soluciona_problemas": forms.DateInput(attrs={"class": "form-control"}),
            "produto_fornecidos": forms.Select(attrs={"class": "form-control"}),
            "fornecedor_acreditado": forms.Select(attrs={"class": "form-control"}),
            "fornecedor_cnpj_ativo": forms.Select(attrs={"class": "form-control"}),
            "desempenha_qualidade": forms.Select(attrs={"class": "form-control"}),
            "custo_beneficio": forms.Select(attrs={"class": "form-control"}),
            "credibilidade": forms.Select(attrs={"class": "form-control"})
        }

class AnexosFornecedoresForm(ModelForm):
    class Meta:
        model = AnexosCliente
        fields = ["anexo"]
        labels = {
            "anexo": "Anexo*",
        }
        widget = {
            "anexo": forms.FileInput(attrs={"class": "form-control"}),
        }