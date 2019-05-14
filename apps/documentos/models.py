from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do documento')
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
