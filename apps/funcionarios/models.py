from django.contrib.auth.models import User
from django.urls import reverse
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.db import models
from django.utils.timezone import now


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100, verbose_name='Função')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='img/perfil', verbose_name='Foto de perfil') #'img_perfil/%Y/%m/%D/'
    data_created = models.DateTimeField(editable=True, null=True, blank=True, default=now, verbose_name='Data cadastro')

    def get_absolute_url(self):
        return reverse('list_funcionario')

    def __str__(self):
        return self.nome + " " + self.sobrenome


