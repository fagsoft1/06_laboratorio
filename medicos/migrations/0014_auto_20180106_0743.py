# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-06 12:43
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0013_remove_especialista_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialista',
            name='firma',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
    ]
