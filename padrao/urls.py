from django.urls import path
from . import views
from . views import *


#Caminhos para as url's do projeto dentro do app instruments


urlpatterns = [
    path('', views.index, name='index_padrao'),
    path('/creategrandeza', GrandezaModelsView.as_view(), name='creategrandeza'),
    path('/listgrandeza', GrandezaListView.as_view(), name='listgrandeza'),
    path('/createunidadeMedida', UnidadeMedidaView.as_view(), name='createunidadeMedida'),
    path('/listunidadeMedida', UnidadeMedidaListView.as_view(), name='listunidadeMedida'),
    path('/resolucaoView', ResolucaoView.as_view(), name='resolucaoView'),
    path('/resolucaoListView', ResolucaoListView.as_view(), name='resolucaoListView'),

    path('/tipoPadraoView', Tipo_PadrãoView.as_view(), name='tipoPadraoView'),
    path('/tipoPadraoListView', Tipo_PadrãoListView.as_view(), name='tipoPadraoListView'),

    path('/FaixasFormView', FaixasFormView.as_view(), name='FaixasFormView'),
    path('/FaixasFormListView', FaixasFormListView.as_view(), name='FaixasFormListView'),
    
    path('/NovoPadraoFormView', Novo_PadrãoFormView.as_view(), name='NovoPadraoFormView'),
    path('/NovoPadraoFormListView', Novo_PadrãoFormListView.as_view(), name='NovoPadraoFormListView'),

    path('/Criterio_AceitacaoView', Criterio_AceitacaoView.as_view(), name='Criterio_AceitacaoView'),
    path('/Criterio_AceitacaoListView', Criterio_AceitacaoListView.as_view(), name='Criterio_AceitacaoListView'),

]
