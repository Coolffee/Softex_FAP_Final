from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Paciente
from .serializers import PacienteSerializer
from .filters import PacienteFilter

class PacientePagination(PageNumberPagination):
    page_size = 10  # Número de objetos por página
    page_size_query_param = 'page_size'
    max_page_size = 100

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PacienteFilter
    pagination_class = PacientePagination