# Generated by Django 5.2 on 2025-04-10 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercicios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercicio',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='exercicio',
            name='imagem_url',
        ),
    ]
