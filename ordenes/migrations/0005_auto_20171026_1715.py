# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0004_orden_medico_remitente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='direccion_contacto_alternativo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Dirección Contacto'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='nombre_contacto_alternativo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre Contacto'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='numero_contacto_alternativo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Número Contacto'),
        ),
    ]