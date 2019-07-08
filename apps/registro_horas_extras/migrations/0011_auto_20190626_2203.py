# Generated by Django 2.2.1 on 2019-06-27 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_horas_extras', '0010_auto_20190626_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrohoraextra',
            name='date_time_final',
        ),
        migrations.RemoveField(
            model_name='registrohoraextra',
            name='date_time_inicial',
        ),
        migrations.AddField(
            model_name='registrohoraextra',
            name='time_he1',
            field=models.DurationField(blank=True, null=True, verbose_name='Tempo total'),
        ),
    ]
