# Generated by Django 2.2.1 on 2019-06-23 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0027_auto_20190623_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='data_modified',
        ),
    ]