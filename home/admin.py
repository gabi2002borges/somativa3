from django.contrib import admin
from .models import Medico, Agendamento


@admin.register(Medico)
class detMedico(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm', 'especialidade', 'foto', 'mostrar')


@admin.register(Agendamento)
class detAgendamento(admin.ModelAdmin):
    list_display = ('data', 'horario', 'medicos', 'mostrar')

