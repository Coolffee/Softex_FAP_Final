import django_filters
from .models import Paciente

class PacienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains')
    data_nascimento = django_filters.DateFilter(field_name='data_nascimento', lookup_expr='exact')

    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento']