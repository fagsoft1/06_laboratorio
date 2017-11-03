# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0012_auto_20171102_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examen',
            name='examen_grupo',
        ),
        migrations.AddField(
            model_name='examen',
            name='examenes',
            field=models.ManyToManyField(blank=True, related_name='_examen_examenes_+', to='examenes.Examen', verbose_name='mis_examenes'),
        ),
    ]
