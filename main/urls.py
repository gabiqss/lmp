from django.urls import path
from . import views

# Caminhos para as url's do projeto dentro do app main

urlpatterns = [
    path("", views.render_main_screen, name="home_screen"),
    path("clientes", views.clientes, name="clientes"),
    path("consultar_empresa", views.consultar_empresa, name="consultar_empresa"),
    path("cadastrar_cliente", views.cadastrar_cliente_cpf, name="cadastrar_cliente_cpf"),
    path("cliente/<int:id>", views.cliente_view, name="view-cliente"),
    path("cliente/<int:id>/edit", views.cliente_edit, name="view-cliente-edit"),
    path("cliente/<int:id>/new_contact", views.novo_contato, name="new-contact"),
    path(
        "cliente/<int:id_cliente>/<int:id_contato>/edit",
        views.editar_contato,
        name="editar-contato",
    ),
    path("exibir_contatos/", views.exibir_contatos, name="exibir_contatos"),
    path("delete/<int:id>", views.delete_cliente, name="delete-cliente"),
    path(
        "cliente/<int:id_cliente>/delete/<int:id_contato>",
        views.delete_contato,
        name="delete-contato",
    ),
    path("fornecedores", views.fornecedores, name="fornecedores"),
    path("cadastrar_fornecedor", views.cadastrar_fornecedor, name="cadastrar_fornecedor"),
    path("cadastrar_fornecedor_cpf", views.cadastrar_fornecedor_cpf, name="cadastrar_fornecedor_cpf")
]
