from django.db import models
import pandas as pd
from ordemS.consts import StatusOs


class Dados(models.Model):
    df = pd.read_csv("staticfiles/data/sectors.csv")
    CHOICES_SETOR = [(i, i) for i in df["NAME"][2:].unique()]
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    fone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    contrato = models.CharField(max_length=100)
    nota_fiscal = models.CharField(max_length=100)
    tipo_envio = models.CharField(max_length=100)
    embalagem = models.CharField(max_length=100)
    data_chamado = models.DateField()
    data_atendimento = models.DateField()
    data_entrada = models.DateField()
    saida_prevista = models.DateField()
    arquivo_pdf = models.FileField(
        upload_to="media/", null=True, blank=True
    )  # Adiciona o campo para o arquivo PDF

    setor = models.CharField(max_length=100, choices=CHOICES_SETOR, default="")

    status = models.CharField(
        choices=StatusOs.choices, max_length=20, default=StatusOs.OPEN
    )

    info_instrumentos = models.TextField()
    observacoes = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.razao_social


class OrdemDeServico(models.Model):
    df = pd.read_csv("staticfiles/data/sectors.csv")
    CHOICES_SETOR = [(i, i) for i in df["NAME"][2:].unique()]
    contrato = models.CharField(max_length=100)
    nota_fiscal = models.CharField(max_length=100)
    tipo_envio = models.CharField(max_length=100)
    embalagem = models.CharField(max_length=100)
    data_chamado = models.DateField()
    data_atendimento = models.DateField()
    data_entrada = models.DateField()
    saida_prevista = models.DateField()
    arquivo_pdf = models.FileField(
        upload_to="media/", null=True, blank=True
    )  # Adiciona o campo para o arquivo PDF
    setor = models.CharField(max_length=100, choices=CHOICES_SETOR, default="")

    status = models.CharField(
        choices=StatusOs.choices, max_length=20, default=StatusOs.OPEN
    )

    info_instrumentos = models.TextField()
    observacoes = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OS {self.equipamento.orcamento.solicitante} - {self.equipamento} - {self.data_cadastro}"
