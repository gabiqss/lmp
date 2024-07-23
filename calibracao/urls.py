from django.urls import path
from . import views

#Caminhos para as url's do projeto dentro do app main

urlpatterns = [
    path('/balanca', views.tabela_view, name='calibracao'),
    path('gerar_pdf/', views.gerar_pdf_view, name='gerar_pdf'),
    path('/trena', views.trena_processo, name='calibracao-trena'),
]