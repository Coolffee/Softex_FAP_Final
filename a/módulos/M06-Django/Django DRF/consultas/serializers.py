from rest_framework import serializers

from .models import Consulta, Paciente, Medico

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'
