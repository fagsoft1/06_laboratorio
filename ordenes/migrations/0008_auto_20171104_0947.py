# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0007_auto_20171104_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenexamen',
            name='valor_resultado',
            field=models.CharField(default='', max_length=300),
        ),
    ]