# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 05:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0007_auto_20171204_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'permissions': [('list_paciente', 'Can list Paciente')], 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
    ]
