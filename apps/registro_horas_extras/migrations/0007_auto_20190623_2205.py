# Generated by Django 2.2.1 on 2019-06-24 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registro_horas_extras', '0006_auto_20190623_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='time_he',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Hora atual'),
        ),
    ]