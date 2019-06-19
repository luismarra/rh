from django.db import models
from django.urls import reverse


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    segmento = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('create_empresa')

    def __str__(self):
        return self.nome
