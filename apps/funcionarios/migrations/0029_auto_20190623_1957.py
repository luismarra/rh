# Generated by Django 2.2.1 on 2019-06-23 22:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0028_remove_funcionario_data_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='data_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
