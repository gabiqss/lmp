from django.urls import path
from . import views

# Caminhos para as url's do projeto dentro do app main

urlpatterns = [
    path("/procedimentos", views.criar_procedimento, name="criar_procedimento"),
]