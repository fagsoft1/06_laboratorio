# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_paciente_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='nro_identificacion',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]