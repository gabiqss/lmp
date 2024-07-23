from django.urls import path
from . import views
from .views import orcamento_update_view, orcamento_create_or_update_view, OrcamentoUpdateView

urlpatterns = [
    path("/orcamentos", views.view_orcamento, name="view-orcamento"),
    path("/solicitante/create", views.create_solicitante, name="add-solictante"),
    path("/orcamento/create/", views.orcamento_create_or_update_view, name="orcamento_create"),
    
    path("/orcamento/<int:pk>/update/", OrcamentoUpdateView.as_view(), name="orcamento_update"),
    path("/<int:id_orcamento>/equipamentos/", views.view_equipamentos, name="orcamento-equipamentos"),
    path("/<int:id_orcamento>/equipamentos/create/", views.create_equipamento, name="create-equipamento"),
    path("/<int:id_orcamento>/pagamento/", views.create_dados_de_pagamento_orcamento, name="pagamento-orcamento"),
    path("/<int:id_orcamento>/orcamento/", views.orcamento_detail_view, name="detail-orcamento"),
    path("/<int:id_orcamento>/orcamento/edit/", views.orcamento_edit_view, name="edit-orcamento"),
    path("/<int:id_orcamento>/orcamento/pdf/", views.orcamento_pdf_view, name="pdf-orcamento"),
    path("/<int:id_orcamento>/orcamento/delete/", views.orcamento_delete_view, name="delete-orcamento"),
    path("/tipo_orcamento/create/", views.tipo_orcamento_create, name="orcamento-type-create"),
    path('buscar_informacoes_banco/', views.buscar_informacoes_banco, name='buscar_informacoes_banco'),
    path('/solicitacao/create/', views.solicitacao_create, name='solicitacao_create'),
    path('/condicao/create/', views.pagamento_condicao_create, name='condicao_create'),
    path('/forma/create/', views.pagamento_forma_create, name='forma_create'),
    path('/solicitacao/delete/<int:id>/', views.delete_solicitacao, name='delete_solicitacao'),
    path('/condicao/delete/<int:id>/', views.delete_pagamento_condicao, name='delete_pagamento_condicao'),
    path('/forma/delete/<int:id>/', views.delete_pagamento_forma, name='delete_pagamento_forma'),
    path('/tipo_orcamento/delete/<int:id>/', views.delete_tipo_orcamento, name='delete_tipo_orcamento'),
    path('/responsavel/delete/<int:id>/', views.delete_responsavel, name='delete_responsavel'),
    path('responsavel/create/', views.responsavel_create, name='create_responsavel'),
    path('/contato/delete/<int:id>/', views.delete_contato, name='delete_contato'),
    path('/cliente/delete/<int:id>/', views.cliente_delete, name='delete_cliente'),
    path('/cliente_cpf/create/', views.cliente_cpf_create, name='add_cpf'),
    path('/cliente_cnpj/create/', views.cliente_cnpj_create, name='add_cnpj'),
    path('/contato/create/', views.contato_create, name='add_contato'),
    path('/calibracao/create/', views.servico_calibracao_create, name='servico_calibracao_create'),
    path('/calibracao/delete/<int:id>/', views.delete_servico_calibracao, name='delete_servico_calibracao'),
    path('/ensaio/create/', views.servico_ensaio_create, name='servico_ensaio_create'),
    path('/ensaio/delete/<int:id>/', views.delete_servico_ensaio, name='delete_servico_ensaio'),
    path('/qt/create/', views.servico_qt_create, name='servico_qt_create'),
    path('/qt/delete/<int:id>/', views.delete_servico_qt, name='delete_servico_qt'),
    path('/manutencao/create/', views.servico_manutencao_create, name='servico_manutencao_create'),
    path('/manutencao/delete/<int:id>/', views.delete_servico_manutencao, name='delete_servico_manutencao'),
    path('/buscar_contatos/', views.buscar_contatos, name='buscar_contatos'),
    path('/orcamento/alteracao/<int:id_orcamento>/', views.orcamento_alterar, name='orcamento_alterar'),
    path('/orcamento/<int:orcamento_id>/atualizar/', orcamento_update_view, name='atualizar-orcamento'),


]
