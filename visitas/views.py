from django.shortcuts import render, redirect, get_object_or_404
from visitas import models
from .models import Visitante
from .forms import VisitanteForm


def visitas(request):
    return render(request, 'visitas/home.html')


def add_visitas(request):
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto Visitante no banco de dados
            # Redireciona para a página de listagem de visitas
            return redirect('visitas:listar_visitas')
    else:
        form = VisitanteForm()

    return render(request, 'visitas/add_visitas.html', {'form': form})


def listar_visitas(request):
    visitantes = Visitante.objects.all()
    return render(request, 'visitas/listar_visitas.html', {'visitantes': visitantes})


def editar_visitas(request, visita_id):
    visitantes = Visitante.objects.all()
    # Recupera o visitante com o ID fornecido ou retorna um erro 404 se não encontrado
    visitante = get_object_or_404(Visitante, id=visita_id)
    if request.method == 'POST':
        # Se o formulário for enviado via POST, atualize os dados do visitante com os novos valores
        visitante.nome = request.POST['nome']
        visitante.doc = request.POST['doc']
        visitante.telefone = request.POST['telefone']

        # Salve as alterações no banco de dados
        visitante.save()

        return redirect('visitas:listar_visitas')

    return render(request, 'visitas/editar_visitas.html', {'visitantes': visitante})


def excluir_visitas(request, visita_id):
    visitante = get_object_or_404(Visitante, pk=visita_id)

    if request.method == 'POST':
        visitante.delete()
        return redirect('visitas:listar_visitas')

    return render(request, 'visitas/excluir_visitas.html', {'visitantes': visitante})
