from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuração da aplicação de contas.

    Esta classe define a configuração da aplicação de contas.

    Attributes:
        default_auto_field (str): O nome do campo automático padrão.
        name (str): O nome da aplicação.
    """
    # English
    """
    Configuration of the accounts app.

    This class defines the configuration of the accounts app.

    Attributes:
        default_auto_field (str): The name of the default auto field.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
