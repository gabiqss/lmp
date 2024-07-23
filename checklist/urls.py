from django.urls import path
from . import views

urlpatterns = [
    path('/create/', views.create_checklist, name='create_checklist'),
    path('', views.checklist_list_view, name='checklist_list'),
    path('/<int:id>', views.checklist, name='checklist'),
]
