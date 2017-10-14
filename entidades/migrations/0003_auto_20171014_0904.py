# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0002_entidad_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoEntidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('enviar_correo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Contacto Entidad',
                'verbose_name_plural': 'Contactos Entidad',
            },
        ),
        migrations.RemoveField(
            model_name='entidad',
            name='codigo_entidad',
        ),
        migrations.RemoveField(
            model_name='entidad',
            name='contacto',
        ),
        migrations.RemoveField(
            model_name='entidad',
            name='correo_electronico',
        ),
        migrations.AddField(
            model_name='contactoentidad',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.Entidad'),
        ),
    ]