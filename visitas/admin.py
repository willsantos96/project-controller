from django.contrib import admin
from .models import Visitante


class VisitanteAdmin (admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone')


admin.site.register(Visitante, VisitanteAdmin)
