from django.shortcuts import render
from visitas import models
from .models import Visitante

def visitas (request):
    return render(request, 'visitas/home.html')

def add_visitas (request):
    return render(request, 'visitas/add_visitas.html')

def listar_visitas (request):
    visitantes = Visitante.objects.all()
    return render(request, 'visitas/listar_visitas.html', {'visitantes': visitantes})

def editar_visitas (request):
    return render(request, 'visitas/editar_visitas.html')

def excluir_visitas (request):
    return render(request, 'visitas/excluir_visitas.html')