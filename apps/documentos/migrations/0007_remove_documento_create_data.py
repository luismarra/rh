# Generated by Django 2.2.1 on 2019-06-18 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0006_documento_create_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='create_data',
        ),
    ]
