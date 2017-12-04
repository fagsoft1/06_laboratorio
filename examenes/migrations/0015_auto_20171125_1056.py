# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0014_remove_examen_examenes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupsCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Cups Categoría',
                'verbose_name_plural': 'Cups Categorías',
            },
        ),
        migrations.CreateModel(
            name='CupsSubGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Cups Sub Grupo',
                'verbose_name_plural': 'Cups Sub Grupos',
            },
        ),
        migrations.RenameModel(
            old_name='AgrupacionExamen',
            new_name='CupsGrupo',
        ),
        migrations.AlterModelOptions(
            name='cupsgrupo',
            options={'verbose_name': 'Cups Grupo', 'verbose_name_plural': 'Cups Grupos'},
        ),
        migrations.AddField(
            model_name='cupssubgrupo',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_subgrupos', to='examenes.CupsGrupo'),
        ),
        migrations.AddField(
            model_name='cupscategoria',
            name='subgrupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_categorias', to='examenes.CupsSubGrupo'),
        ),
    ]
