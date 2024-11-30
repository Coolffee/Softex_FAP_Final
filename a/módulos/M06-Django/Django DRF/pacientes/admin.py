from django.contrib import admin
from .models import Paciente
# Register your models here.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'email', 'telefone', 'endereco')
    search_fields = ('nome', 'email')
    list_filter = ('data_nascimento',)