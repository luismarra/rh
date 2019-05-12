# Generated by Django 2.2.1 on 2019-05-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da empresa', max_length=100)),
                ('segmento', models.CharField(help_text='Segmento da empresa', max_length=200)),
            ],
        ),
    ]
