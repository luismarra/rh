# Generated by Django 2.2.1 on 2019-06-24 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_horas_extras', '0005_auto_20190623_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='time_he',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Hora atual'),
        ),
    ]
