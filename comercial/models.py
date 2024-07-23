from django.db import models
import json

class Estoque(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    sigla = models.CharField(max_length=6)
    setor_destino = models.CharField(max_length=50, null=True, blank=True)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, null=True, blank=True)
    tempo_atividade = models.DurationField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    temperatura = models.TextField(blank=True, null=True)  
    umidade = models.TextField(blank=True, null=True)  
    pressao = models.TextField(blank=True, null=True)  

    fa_registro = models.BooleanField(default=True)
    utilizado_fluxo = models.BooleanField(default=True)
    bloquear_certificado_ko = models.BooleanField(default=False)

    def save_temperatura(self, campos):
        self.temperatura = json.dumps(campos)

    def get_temperatura(self):
        return json.loads(self.temperatura) if self.temperatura else []

    def save_umidade(self, campos):
        self.umidade = json.dumps(campos)

    def get_umidade(self):
        return json.loads(self.umidade) if self.umidade else []

    def save_pressao(self, campos):
        self.pressao = json.dumps(campos)

    def get_pressao(self):
        return json.loads(self.pressao) if self.pressao else []
    
    def __str__(self):
        return self.nome



class AreaAcreditacao(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome