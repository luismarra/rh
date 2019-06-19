# Generated by Django 2.2.1 on 2019-06-16 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0008_auto_20190609_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='ultimonome',
            field=models.CharField(default=1, help_text='Último Nome', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='funcao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(help_text='Primeiro Nome', max_length=100),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
