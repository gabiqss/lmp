from django.db import models
from instruments.models import InstrumentTypes
from main.models import Customers_main
import json



class Procedimento_eletronico(models.Model):
    TIPO_PROCEDIMENTO = [
        ('calibracao', 'Calibração'),
        ('ensaio', 'Ensaio'),
    ]

    TIPO_CALIBRACAO = [
        ('todos', 'Todos'),
        ('ensaio elétrico', 'Ensaio Elétrico'),
        ('rastreado', 'Rastreado'),
        ('rbc', 'RBC'),
    ]

    LOCAL = [
        ('todos', 'Todos'),
        ('laboratorio', 'Laboratório'),
        ('campo', 'Campo (in-company)'),
    ]


    tipo_procedimento = models.CharField(max_length=11, choices=TIPO_PROCEDIMENTO)
    codigo = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    cliente = models.ForeignKey(Customers_main, on_delete=models.CASCADE)
    tipo_instrumento = models.ForeignKey(InstrumentTypes, on_delete=models.CASCADE)
    tipo_calibracao = models.CharField(max_length=20, choices=TIPO_CALIBRACAO)
    local = models.CharField(max_length=20, choices=LOCAL)
    ult_analise_critica = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    periodo_revisao = models.IntegerField(blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class ValoresCalculos(models.Model):
    procedimento = models.ForeignKey(Procedimento_eletronico, on_delete=models.CASCADE)
    valores = models.TextField(blank=True, null=True)  

    def save_valores(self, campos):
        self.valores = json.dumps(campos)

    def get_valores(self):
        return json.loads(self.valores) if self.valores else []
    
    def __str__(self):
        return self.valores