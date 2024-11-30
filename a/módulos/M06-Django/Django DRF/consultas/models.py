from django.db import models

# Create your models here.


class Consulta(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    convenio = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data = models.DateField()
    horario = models.TimeField()
    
    
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    medico = models.CharField(max_length=50)
    crm = models.CharField(max_length=10)
    especialidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Consultas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='consultas')
    def __str__(self):
        return self.paciente