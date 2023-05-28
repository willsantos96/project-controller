from django.db import models
from datetime import date
from django.utils import timezone

class Visitante(models.Model):
    nome = models.CharField(max_length=100)
    doc = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    data_entrada = models.DateField(default=date.today)
    hora_entrada = models.DateTimeField(default=timezone.now)
    data_saida = models.DateField(null=True, blank=True)
    hora_saida = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.nome
