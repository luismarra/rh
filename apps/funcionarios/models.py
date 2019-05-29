from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome completo do funcionário')
    funcao = models.CharField(max_length=100, help_text='Função na empresa')
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='funcionario')
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome


