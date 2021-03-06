# Generated by Django 2.2.1 on 2019-06-27 00:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registro_horas_extras', '0008_auto_20190623_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrohoraextra',
            old_name='time_he',
            new_name='date_time_final',
        ),
        migrations.AddField(
            model_name='registrohoraextra',
            name='date_time_inicial',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data e Hora'),
        ),
        migrations.AlterField(
            model_name='registrohoraextra',
            name='motivo',
            field=models.CharField(max_length=100, verbose_name='Motivo da Hora Extra'),
        ),
    ]
