# Generated by Django 2.2.1 on 2019-06-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0023_auto_20190623_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='dat_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
