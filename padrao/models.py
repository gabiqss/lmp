from django.db import models
from main.models import *
from comercial.models import *
from instruments.models import *

class Grandeza(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Unidade_Medida(models.Model):
    nome = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=5)
    grandeza = models.ForeignKey(Grandeza, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    


class Resolucao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=10)

    def __str__(self):
        return str(self.valor)



class Tipo_Padrão(models.Model):
    nome = models.CharField(max_length=50)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Faixas(models.Model):
    descricao = models.CharField(max_length=250)
    unidade_medida = models.ForeignKey(Unidade_Medida ,on_delete=models.CASCADE)
    amplitude_max = models.IntegerField(blank=True, null=True)
    amplitude_min = models.IntegerField(blank=True, null=True)
    resolucao = models.ForeignKey(Resolucao, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao



class Novo_Padrão(models.Model):
    tag = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50)
    tipo_instrumento = models.ForeignKey(InstrumentTypes, on_delete=models.CASCADE)
    modelo_instrumento = models.ForeignKey(InstrumentsModels, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Customers_main, on_delete=models.CASCADE)
    setor_cliente = models.CharField(max_length=50) #possivel alteração
    prox_calibracao = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    prox_verificacao = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    calibrar_a_cada = models.CharField(max_length=50, blank=True)
    verificar_a_cada = models.CharField(max_length=50, blank=True)
    padrao_status = models.BooleanField(default=True)
    utilizado_campo = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True, null=True)
    calibrar_com = models.ForeignKey(Tipo_Padrão, on_delete=models.CASCADE)
    faixas = models.ManyToManyField(Faixas)

    def __str__(self):
        return self.tag
    

class Criterio_Aceitacao(models.Model):

    TIPO_FORMULA = [
        ('erro', 'Erro'),
        ('erro + incert', 'Erro + Incerteza'),
        ('incerteza', 'Incerteza'),
        ('percent', 'Percentual do ponto lido'),
    ]

    nome = models.CharField(max_length=50)
    formula_de_validacao = models.CharField(max_length=50, choices=TIPO_FORMULA)
    grandeza = models.ForeignKey(Grandeza, on_delete=models.CASCADE)
    unidade_medida = models.ForeignKey(Unidade_Medida, on_delete=models.CASCADE)
    amplitude_max = models.IntegerField(blank=True, null=True)
    amplitude_min = models.IntegerField(blank=True, null=True)
    limite_max = models.IntegerField(blank=True, null=True)
    limite_min = models.IntegerField(blank=True, null=True)
    padrao_id = models.ForeignKey(Novo_Padrão, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome