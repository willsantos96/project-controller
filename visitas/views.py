from django.shortcuts import render
from visitas import models

def visitas (request):
    return render(request, 'base.html')
