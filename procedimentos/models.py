from django.db import models
from main.models import *


class Dados_procedimento(models.Model):
    codigo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.titulo

class ArquivoPDF(models.Model):
    procedimento = models.ForeignKey(Dados_procedimento, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='arquivos_proced', max_length=100)



