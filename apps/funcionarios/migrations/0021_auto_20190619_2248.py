# Generated by Django 2.2.1 on 2019-06-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0020_auto_20190619_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/perfil'),
        ),
    ]
