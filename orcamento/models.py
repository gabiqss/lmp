from django.db import models
from orcamento.consts import (
    FormaDePagamentoChoices,
    GarantiaChoices,
    ModoDePagamentoChoices,
    TiposDeServicosChoices,
)
from django.core.validators import MinValueValidator
from orcamento.consts import StatusOrcamentos
from instruments.models import InstrumentsInstruments
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Orcamento(models.Model):
    orcamento_raiz = models.IntegerField(blank=True, null=True)
    solicitante = models.ForeignKey("main.Customers_main", on_delete=models.CASCADE, blank=True, null=True)
    contato = models.ForeignKey("main.Contacts_Customers", on_delete=models.CASCADE, blank=True, null=True)
    responsavel = models.ForeignKey(
        "accounts.CustomUser", on_delete=models.CASCADE, blank=True, null=True
    )
    data_cadastro = models.DateTimeField(null=True, blank=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    validade_proposta = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(max_length=250, blank=True, null=True)
    forma_pagamento = models.CharField(max_length=250, null=True, blank=True)
    local = models.CharField(max_length=250, null=True, blank=True)
    contrato = models.CharField(max_length=250, null=True, blank=True)
    tipo_de_desconto = models.CharField(
        max_length=250, null=True, blank=True
    )
    desconto = models.CharField(max_length=250, null=True, blank=True)
    acrescimo = models.CharField(max_length=250, null=True, blank=True)
    condicao_pagamento = models.CharField(
        max_length=250, null=True, blank=True
    )
    tipo_orcamento = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )
    forma_solicitacao = models.CharField(
        max_length=250, null=True, blank=True
    )
    status = models.CharField(
        max_length=20, default=StatusOrcamentos.OPEN
    )

    
    def __str__(self):
        return f"Solicitação do {self.solicitante} para {self.contato}"
    
class OrcamentoAtividade(models.Model):
    solicitante = models.ForeignKey("main.Customers_main", on_delete=models.CASCADE, blank=True, null=True)
    contato = models.ForeignKey("main.Contacts_Customers", on_delete=models.CASCADE, blank=True, null=True)
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, blank=True, null=True)
    responsavel_atividade = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='responsavel_atividade_set', blank=True, null=True
    )
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='responsavel_orcamento_set', blank=True, null=True
    )
    data_cadastro = models.DateTimeField(null=True, blank=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    validade_proposta = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(max_length=250, blank=True, null=True)
    forma_pagamento = models.CharField(max_length=250, null=True, blank=True)
    local = models.CharField(max_length=250, null=True, blank=True)
    contrato = models.CharField(max_length=250, null=True, blank=True)
    tipo_de_desconto = models.CharField(
        max_length=250, null=True, blank=True
    )
    desconto = models.CharField(max_length=250, null=True, blank=True)
    acrescimo = models.CharField(max_length=250, null=True, blank=True)
    condicao_pagamento = models.CharField(
        max_length=250, null=True, blank=True
    )
    tipo_orcamento = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )
    forma_solicitacao = models.CharField(
        max_length=250, null=True, blank=True
    )
    status = models.CharField(
        choices=StatusOrcamentos.choices, max_length=20, default=StatusOrcamentos.OPEN
    )

    def __str__(self):
        return f"Solicitação do {self.solicitante} para {self.contato}"
    
class AnexosOrcamento(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, null=True, blank=True)
    anexo = models.FileField(upload_to='anexos_orcamentos/', null=True, blank=True)

class AnexosOrcamentoAtividade(models.Model):
    atividade = models.ForeignKey(OrcamentoAtividade, on_delete=models.CASCADE, null=True, blank=True)
    anexo = models.FileField(upload_to='anexos_orcamentos/', null=True, blank=True)

class ServicosOrcamento(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, null=True, blank=True)
    codigo = models.CharField(max_length=250, blank=True, null=True)
    area_acreditacao = models.CharField(max_length=250, blank=True, null=True)
    especificacao = models.CharField(max_length=250, blank=True, null=True)
    tipo_servico = models.CharField(max_length=250, blank=True, null=True)
    local = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=1000,blank=True, null=True)
    valor = models.CharField(max_length=250,blank=True, null=True)
    pontos = models.CharField(max_length=250,blank=True, null=True)
    pontos_valor_adicional = models.CharField(max_length=250,blank=True, null=True)
    tipo_calibracao = models.CharField(max_length=250, blank=True, null=True)
    tipo_item = models.CharField(max_length=250, blank=True, null=True)

class ServicosOrcamentoAtividade(models.Model):
    atividade = models.ForeignKey(OrcamentoAtividade, on_delete=models.CASCADE, null=True, blank=True)
    codigo = models.CharField(max_length=250, blank=True, null=True)
    area_acreditacao = models.CharField(max_length=250, blank=True, null=True)
    especificacao = models.CharField(max_length=250, blank=True, null=True)
    tipo_servico = models.CharField(max_length=250, blank=True, null=True)
    local = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=1000,blank=True, null=True)
    valor = models.CharField(max_length=250,blank=True, null=True)
    pontos = models.CharField(max_length=250,blank=True, null=True)
    pontos_valor_adicional = models.CharField(max_length=250,blank=True, null=True)
    tipo_calibracao = models.CharField(max_length=250, blank=True, null=True)
    tipo_item = models.CharField(max_length=250, blank=True, null=True)
    
class TipoOrcamento(models.Model):
    tipo = models.CharField(max_length=250)

    def __str__(self):
        return self.tipo
    
class Solicitacao(models.Model):
    meio_solicitacao = models.CharField(max_length=250)

    def __str__(self):
        return self.meio_solicitacao
    
class PagamentoCondicao(models.Model):
    condicao = models.CharField(max_length=250)

    def __str__(self):
        return self.condicao
    
class PagamentoForma(models.Model):
    forma = models.CharField(max_length=250)

    def __str__(self):
        return self.forma
    
class ServicoCalibracao(models.Model):
    codigo = models.CharField(max_length=250, blank=True, null=True)
    area_acreditacao = models.CharField(max_length=250, blank=True, null=True)
    especificacao = models.CharField(max_length=250, blank=True, null=True)
    tipo_calibracao = models.CharField(max_length=250, blank=True, null=True)
    tipo_item = models.CharField(max_length=250, blank=True, null=True)
    local = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=1000,blank=True, null=True)
    pontos = models.CharField(max_length=250,blank=True, null=True)
    pontos_valor_adicional = models.CharField(max_length=250,blank=True, null=True)
    valor = models.CharField(max_length=250,blank=True, null=True)

    def __str__(self):
        return self.codigo
    
class ServicoManutencao(models.Model):
    codigo = models.CharField(max_length=250, blank=True, null=True)
    area_acreditacao = models.CharField(max_length=250, blank=True, null=True)
    especificacao = models.CharField(max_length=250, blank=True, null=True)
    tipo_servico = models.CharField(max_length=250, blank=True, null=True)
    local = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=1000,blank=True, null=True)
    valor = models.CharField(max_length=250,blank=True, null=True)

    def __str__(self):
        return self.codigo
    
class ServicoEnsaio(models.Model):
    codigo = models.CharField(max_length=250, blank=True, null=True)
    area_acreditacao = models.CharField(max_length=250, blank=True, null=True)
    especificacao = models.CharField(max_length=250, blank=True, null=True)
    tipo_servico = models.CharField(max_length=250, blank=True, null=True)
    local = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=1000,blank=True, null=True)
    valor = models.CharField(max_length=250,blank=True, null=True)

    def __str__(self):
        return self.codigo
    
class ServicoQT(models.Model):
    codigo = models.CharField(max_length=250, blank=True, null=True)
    area_acreditacao = models.CharField(max_length=250, blank=True, null=True)
    especificacao = models.CharField(max_length=250, blank=True, null=True)
    tipo_servico = models.CharField(max_length=250, blank=True, null=True)
    local = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=1000,blank=True, null=True)
    valor = models.CharField(max_length=250,blank=True, null=True)

    def __str__(self):
        return self.codigo
    