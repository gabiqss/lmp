from django.db.models import TextChoices


# Dinheiro, Cartão de crédito, Boleto bancário, Pix e Cartão de débito)
class FormaDePagamentoChoices(TextChoices):
    DINHEIRO = "Dinheiro"
    CARTAO_DE_CREDITO = "Cartão de crédito"
    BOLETO = "Boleto bancário"
    PIX = "Pix"

    
class GarantiaChoices(TextChoices):
    SIM = "Sim"
    NAO = "Não"

class TiposDeServicosChoices(TextChoices):
    INSTALACAO = "Instalação"
    CALIBRAÇÃO = "Calibração"
    MANUTENCAO = "Manutenção"
    VENDA = "Venda"


class ModoDePagamentoChoices(TextChoices):
    AVISTA = "À vista"
    PARCELADO = "Parcelado"
    

class StatusOrcamentos(TextChoices):
    OPEN = "Aberto"
    AWAIT_PAYMENT = "Aguardando pagamento"
    MADE_PAYMENT = "Pagamento realizado"
    CANCELED = "Cancelado" 