from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="comercial"),
    path("/criar_estoque", views.criar_estoque, name="criar_estoque"),
    path("/criar_setor", views.criar_setor, name="criar_setor"),
    path("/area_acreditacao", views.area_acreditacao, name="area_acreditacao"),


]