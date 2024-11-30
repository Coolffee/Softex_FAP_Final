from django.urls import path, include
from .views import  ConsultaViewSet, PacienteViewSet, MedicoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]



def create(self, request):
    serializer = PacienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
'''
{    "paciente": "João B",
    "cpf": "12345678901",
    "rg": "1234567",
    "data_nascimento": "1990-01-01",
    "telefone": "11987654321",
    "email": "joao.B@example.com",
    "endereco": "Rua Exemplo",
    "numero": "123",
    "bairro": "Centro",
    "cidade": "São Paulo",
    "estado": "SP",
    "cep": "01001000"
}
'''