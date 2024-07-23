from django.db import models

# Modelo da base de dados de clientes


class Customers_main(models.Model):
    """
    Model representing a customer.
    """

    CREDITO = "CR"
    DEBITO = "DB"
    CHOICES = (
        (CREDITO, "Crédito"),
        (DEBITO, "Débito"),
    )

    name = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    cnpj = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    cpf = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    corporate_name = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    municipal_registration = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    state_registration = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    city = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    uf = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    cep = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    fax = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    neighborhood = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    date_of_fundation = models.CharField(
        null=True, 
        blank=True, 
        max_length=12)
    web_site = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    id_market_segment = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    TIPO_PORTE = [
        ('pequeno porte', 'Pequeno porte'),
        ('medio porte', 'Médio porte'),
        ('grande porte', 'Grande porte'),
    ]
    id_size = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    address_number = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    address_complement = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    payment_day = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    is_requestor_in_field = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    payment_venc = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    company_responsible = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    credit_or_debit_card = models.CharField(
        null=True,
        blank=True,
        max_length=2,
        choices=CHOICES,
        default=CREDITO,
    )

    TIPO_CLIENTE = [
        ('cliente', 'Cliente'),
        ('cliente/fabricante', 'Cliente/Fabricante'),
    ]
    
    tipo_cliente = models.CharField(max_length=50, choices=TIPO_CLIENTE, default='cliente')

    def save(self, *args, **kwargs):
        """
        Override the save method to autoincrement the ID field.
        """

        if not self.id:
            last_customer = Customers_main.objects.last()
            self.id = last_customer.id + 1 if last_customer else 1
        super().save(*args, **kwargs)

    def __str__(
        self,
    ):
        """
        String for representing the Customer object (name).
        """
        return self.name


class AnexosCliente(models.Model):
    cliente = models.ForeignKey(Customers_main, on_delete=models.CASCADE, null=True, blank=True)
    anexo = models.FileField(upload_to='anexos_clientes/', null=True, blank=True)

# Modelo da base de dados de contatos de clientes


class Contacts_Customers(models.Model):
    """
    Model representing a contact associated with a customer.
    """

    name = models.CharField(max_length=250, null=False, blank=False)
    sector = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    commercial_phone = models.CharField(max_length=250, blank=True, default="-")
    cellular = models.CharField(max_length=250, blank=True, default="-")
    description = models.CharField(max_length=100, blank=True, default="-")
    id_customer = models.ForeignKey(Customers_main, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=250, null=True, blank=True)

    def __str__(
        self,
    ):
        """
        String for representing the Contact object (name).
        """
        return self.name


# Modelo da base de dados de setor do cliente


class CustomerSectors(models.Model):
    """
    Model representing sectors of customers.
    """

    id_customer = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    acronym = models.TextField(blank=True, null=True)
    phone = models.FloatField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)


# Modelo da base de dados de contatos


class Contatos(models.Model):
    """
    Model representing contacts in the database.
    """

    nome = models.CharField(max_length=255)
    setor = models.CharField(max_length=255)
    ramal = models.CharField(max_length=10)
    telefone_comercial = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    data_nasc = models.DateField()

    def __str__(self):
        """
        Return a string representation of the contact's name.
        """

        return self.nome


# Modelo da base de dados de fornecedores


class Suppliers(models.Model):
    """
    Model representing suppliers in the database.
    """
    
    name = models.TextField(blank=True, null=True)
    cnpj = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    web_site = models.TextField(blank=True, null=True)
    corporate_name = models.TextField(blank=True, null=True)
    municipal_registration = models.TextField(blank=True, null=True)
    state_registration = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    id_city = models.FloatField(blank=True, null=True)
    id_neighborhood = models.FloatField(blank=True, null=True)
    id_state = models.FloatField(blank=True, null=True)
    cep = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_laboratory = models.IntegerField(blank=True, null=True)
    is_manufacturer = models.IntegerField(blank=True, null=True)
    removed = models.IntegerField(blank=True, null=True)
    date_of_fundation = models.TextField(blank=True, null=True)
    is_carrier = models.FloatField(blank=True, null=True)
    agency = models.FloatField(blank=True, null=True)
    account_number = models.FloatField(blank=True, null=True)
    id_bank = models.FloatField(blank=True, null=True)
    is_abstract_person = models.IntegerField(blank=True, null=True)
    stock_expression = models.FloatField(blank=True, null=True)
    address_number = models.TextField(blank=True, null=True)
    address_complement = models.TextField(blank=True, null=True)
    is_approved = models.FloatField(blank=True, null=True)
    identifier = models.TextField(blank=True, null=True)
    id_evaluation_status = models.IntegerField(blank=True, null=True)

class Fornecedores(models.Model):
    """
    Model representing suppliers in the database.
    """
    
    CREDITO = "CR"
    DEBITO = "DB"
    CHOICES = (
        (CREDITO, "Crédito"),
        (DEBITO, "Débito"),
    )

    name = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    cnpj = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    cpf = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    corporate_name = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    municipal_registration = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    state_registration = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    uf = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    cep = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    fax = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    neighborhood = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    date_of_fundation = models.CharField(
        null=True, 
        blank=True, 
        max_length=12)
    web_site = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    id_market_segment = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    TIPO_PORTE = [
        ('pequeno porte', 'Pequeno porte'),
        ('medio porte', 'Médio porte'),
        ('grande porte', 'Grande porte'),
    ]
    id_size = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    address_number = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    address_complement = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    payment_day = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    is_requestor_in_field = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    payment_venc = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    company_responsible = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    credit_or_debit_card = models.CharField(
        null=True,
        blank=True,
        max_length=2,
        choices=CHOICES,
        default=CREDITO,
    )

    TIPO_CLIENTE = [
        ('fabricante', 'Fabricante'),
        ('cliente/fabricante', 'Cliente/Fabricante'),
    ]
    
    tipo_cliente = models.CharField(max_length=50, choices=TIPO_CLIENTE, default='fabricante')

    SIM_NAO = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

    retorna_rapidamente = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        choices=SIM_NAO
    )

    data_retorna_rapidamente = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )

    soluciona_problemas = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        choices=SIM_NAO
    )

    data_soluciona_problemas = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )

    PRODUTO_FORNECIDO = [
        ('calibracao', 'Calibração'),
        ('produto', 'Produto'),
        ('material_de_referencia', 'Material de Referência'),
        ('PEP', 'PEP'),
        ('certificador', 'Certificador'),
        ('outros', 'Outros'),
    ]

    produto_fornecidos = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        choices=PRODUTO_FORNECIDO
    )

    SIM_NAO_NA = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
        ('n/a', 'N/A'),
    ]

    fornecedor_acreditado = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        choices=SIM_NAO_NA
    )

    fornecedor_cnpj_ativo = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        choices=SIM_NAO_NA
    )

    desempenha_qualidade = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        choices=SIM_NAO
    )

    SATISFACAO = [
        ('satisfatorio', 'Satisfatório'),
        ('insatisfatorio', 'Insatisfatório'),
    ]

    custo_beneficio = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        choices=SATISFACAO
    )

    credibilidade = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        choices=SATISFACAO
    )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
    
class AnexosFornecedores(models.Model):
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, null=True, blank=True)
    anexo = models.FileField(upload_to='anexos_fornecedores/', null=True, blank=True)