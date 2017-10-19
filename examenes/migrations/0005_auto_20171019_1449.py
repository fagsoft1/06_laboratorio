# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0004_auto_20171007_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgrupacionExamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Exámen Agrupado',
                'verbose_name_plural': 'Examenes Agrupados',
            },
        ),
        migrations.AlterModelOptions(
            name='examen',
            options={'verbose_name': 'Exámen', 'verbose_name_plural': 'Examenes'},
        ),
    ]
