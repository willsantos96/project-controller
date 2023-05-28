from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'visitas'

urlpatterns = [
    path('', views.visitas, name='home'),
    path('add_visitas/', views.add_visitas, name='add_visitas'),
    path('listar_visitas/', views.listar_visitas, name='listar_visitas'),
    path('editar_visitas/', views.editar_visitas, name='editar_visitas'),
    path('excluir_visitas/', views.excluir_visitas, name='excluir_visitas'),
]
