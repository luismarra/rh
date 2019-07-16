from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario
from django.utils.timezone import now
from django.db.models import Sum, Avg, Count


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, verbose_name='Motivo da Hora Extra')
    observacao = models.TextField(max_length=500, verbose_name='Observação')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    date_time_he = models.DateTimeField(
            editable=True,
            null=True,
            blank=True,
            default=now,
            verbose_name='Data e Hora Inicial')
    time_he1 = models.DurationField(blank=True, null=True, verbose_name='Tempo total')

    def time_he1_duration_HHmm(self):
        sec = self.time_he1.total_seconds()
        return '%02d:%02d' % (int((sec / 3600) % 3600), int((sec / 60) % 60))

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.funcionario.id])

    def __str__(self):
        return self.motivo
