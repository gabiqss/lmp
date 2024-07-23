from django.urls import path
from .views import ordem_servico, editar_ordem_servico

urlpatterns = [
    path('/os', ordem_servico, name='os'),
    path('/os/<int:id>/edit/', editar_ordem_servico, name='ordem-servico-edit'),

]