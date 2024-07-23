from django.urls import path
from . import views
from . views import *

# Caminhos para as url's do projeto dentro do app main

urlpatterns = [
    path("", views.index_procedimentoElet, name="criar_procedimentos_eletronicos"),
    path('create_procedimentos', ProcElet_Create.as_view(), name='create_procedimentoEletr'),
    path('list_procedimentos', ProcElet_ListView.as_view(), name='list_procedimentoEletr'),
    path('/valores_calculo', views.valores_calculo, name='valores_calculo'),

]