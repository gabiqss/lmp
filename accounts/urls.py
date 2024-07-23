from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('/registro', views.registro, name='registro'),
    path('/logout', views.my_logout, name='logout'),
    path('/profile', views.profile, name='profile'),
    path('/colaboradores', views.colaboradores, name='colaboradores'),
    path('/delete_colaborador/<int:id>', views.delete_colaborador, name='delete_colaborador'),
    path('/create_colaborador', views.create_colaborador, name='create_colaborador'),
    path('/edit_colaborador/<int:id>', views.edit_colaborador, name='edit_colaborador'),
    path('/detalhes_colaborador/<int:id>', views.colaborador_detail_view, name='detalhes_colaborador'),

]

"""
Os padrões de URL para o aplicativo accounts.

Este módulo define os padrões de URL para as views no aplicativo accounts. Cada padrão de URL
mapeia um caminho de URL para uma função de visualização específica.

Padrões de URL:
- Login: '/'
- Registro de Usuário: '/registro'
- Logout: '/logout'
- Perfil do Usuário: '/profile'
- Lista de Colaboradores: '/colaboradores'
- Excluir Colaborador: '/delete_colaborador/<int:id>'
- Criar Colaborador: '/create_colaborador'
- Editar Colaborador: '/edit_colaborador/<int:id>'
"""
# English
"""
The URL patterns for the accounts app.

This module defines the URL patterns for the views in the accounts app. Each URL pattern
maps a URL path to a specific view function.

URL patterns:
- Login: '/'
- User Registration: '/registro'
- Logout: '/logout'
- User Profile: '/profile'
- Collaborators List: '/colaboradores'
- Delete Collaborator: '/delete_colaborador/<int:id>'
- Create Collaborator: '/create_colaborador'
- Edit Collaborator: '/edit_colaborador/<int:id>'
"""