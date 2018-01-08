# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-06 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0029_ordenexamenfirmas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.PositiveIntegerField(choices=[(0, 'Creado'), (1, 'Pagado')], default=0),
        ),
        migrations.AlterField(
            model_name='ordenexamen',
            name='examen_estado',
            field=models.PositiveIntegerField(choices=[(0, 'En Proceso'), (1, 'Con Resultados'), (2, 'Verificado'), (3, 'Impreso')], default=0),
        ),
    ]