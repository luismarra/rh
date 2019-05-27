from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    segmento = models.CharField(max_length=200, help_text='Segmento da empresa')

    def __str__(self):
        return self.nome
