# Generated by Django 2.2.1 on 2019-06-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_horas_extras', '0002_registrohoraextra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='time_he',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registrohoraextra',
            name='time_he1',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
