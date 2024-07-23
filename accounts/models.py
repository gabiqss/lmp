from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Anexo(models.Model):
    """
    Modelo para armazenar anexos de usuários.

    Este modelo define um campo para armazenar arquivos anexos relacionados aos usuários do sistema.

    Attributes:
        arquivo (FileField): Campo para armazenar o arquivo anexo.
    """
    # English
    """
    Model for file attachments.

    This model represents file attachments in the system.

    Attributes:
        arquivo (FileField): The file field for storing attachments.
    """
    arquivo = models.FileField(upload_to='anexos/')

class CustomUserManager(BaseUserManager):
    """
    Gerenciador de usuários personalizado.

    Este gerenciador fornece métodos para criar usuários e superusuários personalizados.

    Methods:
        create_user(username, email, password=None, **extra_fields): Cria um novo usuário.
        create_superuser(username, email, password=None, **extra_fields): Cria um novo superusuário.
    """
    # English
    """
    Custom user manager.

    This manager provides methods for creating custom users and superusers.

    Methods:
        create_user(username, email, password=None, **extra_fields): Creates a new user.
        create_superuser(username, email, password=None, **extra_fields): Creates a new superuser.
    """
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Cria um novo usuário.

        Args:
            username (str): Nome de usuário.
            email (str): Endereço de e-mail do usuário.
            password (str, optional): Senha do usuário. Defaults to None.
            **extra_fields (dict): Outros campos personalizados do usuário.

        Returns:
            CustomUser: O usuário recém-criado.
        """
        # English
        """
        Creates a new user.

        Args:
            username (str): Username.
            email (str): Email address of the user.
            password (str, optional): Password of the user. Defaults to None.
            **extra_fields (dict): Other custom fields of the user.

        Returns:
            CustomUser: The newly created user.
        """
        user = self.model.objects.create(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Cria um novo superusuário.

        Args:
            username (str): Nome de usuário.
            email (str): Endereço de e-mail do superusuário.
            password (str, optional): Senha do superusuário. Defaults to None.
            **extra_fields (dict): Outros campos personalizados do superusuário.

        Returns:
            CustomUser: O superusuário recém-criado.
        """
        # English
        """
        Creates a new superuser.

        Args:
            username (str): Username.
            email (str): Email address of the superuser.
            password (str, optional): Password of the superuser. Defaults to None.
            **extra_fields (dict): Other custom fields of the superuser.

        Returns:
            CustomUser: The newly created superuser.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    """
    Modelo de usuário personalizado.

    Este modelo estende o modelo AbstractUser fornecido pelo Django para adicionar campos personalizados.

    Attributes:
        full_name (CharField): Nome completo do usuário.
        date_of_birth (DateField): Data de nascimento do usuário.
        sexo (CharField): Sexo do usuário.
        cep (CharField): CEP do usuário.
        numero (CharField): Número do endereço do usuário.
        complemento (CharField): Complemento do endereço do usuário.
        bairro (CharField): Bairro do usuário.
        cidade (CharField): Cidade do usuário.
        estado (CharField): Estado do usuário.
        celular (CharField): Número de celular do usuário.
        rg (CharField): RG do usuário.
        cpf (CharField): CPF do usuário.
        habilitacao (CharField): Habilitação do usuário.
        pis (CharField): PIS do usuário.
        cargo (CharField): Cargo do usuário.
        setor (CharField): Setor do usuário.
        data_admissao (DateField): Data de admissão do usuário.
        data_desligamento (DateField): Data de desligamento do usuário.
        remuneracao (CharField): Remuneração do usuário.
        vale_transporte (CharField): Vale transporte do usuário.
        nome_conjuge (CharField): Nome do cônjuge do usuário.
        rg_conjuge (CharField): RG do cônjuge do usuário.
        cpf_conjuge (CharField): CPF do cônjuge do usuário.
        celular_conjuge (CharField): Número de celular do cônjuge do usuário.
        anexos (ManyToManyField): Anexos associados ao usuário.
        is_active (BooleanField): Indica se o usuário está ativo ou não.
    """
    # English
    """
    Custom user model.

    This model extends the default Django user model with additional fields.

    Attributes:
        full_name (CharField): The full name of the user.
        date_of_birth (DateField): The date of birth of the user.
        sexo (CharField): The gender of the user.
        cep (CharField): The zip code of the user.
        numero (CharField): The number of the user's address.
        complemento (CharField): The complement of the user's address.
        bairro (CharField): The neighborhood of the user's address.
        cidade (CharField): The city of the user's address.
        estado (CharField): The state of the user's address.
        celular (CharField): The phone number of the user.
        rg (CharField): The RG of the user.
        cpf (CharField): The CPF of the user.
        habilitacao (CharField): The driver's license of the user.
        pis (CharField): The PIS of the user.
        cargo (CharField): The position of the user.
        setor (CharField): The department of the user.
        data_admissao (DateField): The admission date of the user.
        data_desligamento (DateField): The dismissal date of the user.
        remuneracao (CharField): The remuneration of the user.
        vale_transporte (CharField): The transportation allowance of the user.
        nome_conjuge (CharField): The spouse's name of the user.
        rg_conjuge (CharField): The spouse's RG of the user.
        cpf_conjuge (CharField): The spouse's CPF of the user.
        celular_conjuge (CharField): The spouse's phone number of the user.
        anexos (ManyToManyField): The attachments associated with the user.
        is_active (BooleanField): Indicates whether the user is active.
    """
    # Adicionando campos personalizados
    full_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], null=True, blank=True)
    cep = models.CharField(max_length=11, null=True, blank=True)
    numero = models.CharField(max_length=5, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    rg = models.CharField(max_length=15, null=True, blank=True)
    cpf = models.CharField(max_length=15, null=True, blank=True)
    habilitacao = models.CharField(max_length=255, null=True, blank=True)
    pis = models.CharField(max_length=255, null=True, blank=True)
    cargo = models.CharField(max_length=255, null=True, blank=True)
    setor = models.CharField(max_length=255, null=True, blank=True)
    data_admissao = models.DateField(null=True, blank=True)
    data_desligamento = models.DateField(null=True, blank=True)
    remuneracao = models.CharField(max_length=255, null=True, blank=True)
    vale_transporte = models.CharField(max_length=255, null=True, blank=True)
    nome_conjuge = models.CharField(max_length=255, null=True, blank=True)
    rg_conjuge = models.CharField(max_length=255, null=True, blank=True)
    cpf_conjuge = models.CharField(max_length=255, null=True, blank=True)
    celular_conjuge = models.CharField(max_length=255, null=True, blank=True)
    anexos = models.ManyToManyField(Anexo, blank=True)
    foto = models.ImageField(upload_to='fotos_colaboradores/', null=True, blank=True)
    # Configurando o is_active como False por padrão
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()  # Adicionando esta linha

    def __str__(self):
        """
        Retorna uma representação de string do usuário.

        Returns:
            str: O nome completo do usuário.
        """
        # English
        """
        Returns a string representation of the user.

        Returns:
            str: The full name of the user.
        """
        return self.full_name

class AnexosColaborador(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    anexo = models.FileField(upload_to='anexos_colaborador/', null=True, blank=True)