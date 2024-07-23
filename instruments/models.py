from django.db import models
from procedimentos.models import Dados_procedimento
from comercial.models import Setor, AreaAcreditacao
from main.models import CustomerSectors, Customers_main, Suppliers

#Modelo da base de dados de instrumentos


#Modelo da base de dados de tipos de instrumentos
    
class InstrumentTypes(models.Model):
    nome = models.CharField(max_length=50)
    procedimento = models.ManyToManyField(Dados_procedimento, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True)
    area_acreditaco = models.ForeignKey(AreaAcreditacao, on_delete=models.CASCADE, null=True, blank=True)
    faixas_padronizadas = models.BooleanField(default=False)
    condicoes_ambientais_temp = models.DecimalField(max_digits=7, decimal_places=2)
    condicoes_ambientais_umi = models.DecimalField(max_digits=7, decimal_places=2)
    condicoes_ambientais_pre = models.DecimalField(max_digits=7, decimal_places=2)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome





# Modelo da base de dados de modelos de instrumentos

class InstrumentsModels(models.Model):
    name = models.CharField(max_length=50)
    instrument_type = models.ForeignKey(InstrumentTypes, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

#Modelo da base de dados de modelos de faixas dos instrumentos

class InstrumentsBands(models.Model):
    id_instrument = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    min_value = models.FloatField(blank=True, null=True)
    max_value = models.FloatField(blank=True, null=True)
    precision = models.FloatField(blank=True, null=True)
    id_measurement = models.FloatField(blank=True, null=True)
    row_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instruments_bands'



class InstrumentsInstruments(models.Model):
    code = models.CharField(max_length=250,blank=True, null=True)
    id_customer = models.ForeignKey(Customers_main, on_delete=models.CASCADE, blank=True, null=True)
    serial_number = models.CharField(max_length=250,blank=True, null=True)
    is_active = models.CharField(max_length=250,blank=True, null=True)
    calibration_frequency_months = models.CharField(max_length=250,blank=True, null=True)
    id_instrument_model = models.ForeignKey(InstrumentsModels, on_delete=models.CASCADE, blank=True, null=True)
    id_current_sector = models.ForeignKey(CustomerSectors, on_delete=models.CASCADE, blank=True, null=True)
    id_instrument_type = models.ForeignKey(InstrumentTypes, on_delete=models.CASCADE, blank=True, null=True)
    id_supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, blank=True, null=True)
    next_calibration = models.DateField(blank=True, null=True)
    tag = models.CharField(max_length=250,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
 
    def __str__(self,):
        return self.code
    