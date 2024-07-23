from django.urls import path
from . import views
from .views import InstrumentTypeCreateView, InstrumentTypeListView, InstrumentsModelsView, InstrumentModelListView


#Caminhos para as url's do projeto dentro do app instruments


urlpatterns = [
    
    path('instruments/cadastro_instrumentos', views.cadastro_instrumento, name='cadastro_instrumento'),    
    path('/instruments', views.instrumento_cliente, name='instrumentos'),
    path('/tipocreate', InstrumentTypeCreateView.as_view(), name='instrument_type_create'),
    path('/tipolist', InstrumentTypeListView.as_view(), name='instrument_type_list'),
    path('/createmodel', InstrumentsModelsView.as_view(), name='instrument_model_create'),
    path('/listmodel', InstrumentModelListView.as_view(), name='instrument_model_list'),

]
