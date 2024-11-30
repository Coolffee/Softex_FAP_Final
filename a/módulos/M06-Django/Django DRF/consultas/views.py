from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Consulta, Paciente, Medico
from .serializers import ConsultaSerializer, PacienteSerializer, MedicoSerializer
from rest_framework import viewsets

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ConsultaListView(APIView):
    def get(self, request):
        consultas = Consulta.objects.all()
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data)
    
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer