# Generated by Django 2.2.1 on 2019-06-20 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0017_auto_20190619_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='img',
            new_name='image',
        ),
    ]
