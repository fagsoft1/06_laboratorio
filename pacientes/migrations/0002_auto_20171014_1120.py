# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email_2',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]