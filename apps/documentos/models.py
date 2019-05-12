from django.db import models


class Documento(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do documento')

    def __str__(self):
        return self.nome
