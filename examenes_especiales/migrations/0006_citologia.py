# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0034_auto_20180113_0953'),
        ('examenes_especiales', '0005_auto_20180113_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('es_insatisfactoria', models.BooleanField(default=False)),
                ('debe_repetir', models.BooleanField(default=False)),
                ('con_componente_endocervical', models.BooleanField(default=False)),
                ('celularidad_escasa', models.BooleanField(default=False)),
                ('mala_tincion', models.BooleanField(default=False)),
                ('hemorragico', models.BooleanField(default=False)),
                ('mala_fijacion', models.BooleanField(default=False)),
                ('fondo_con_leucocitos', models.BooleanField(default=False)),
                ('trichomonas', models.BooleanField(default=False)),
                ('herpes', models.BooleanField(default=False)),
                ('candida_sp', models.BooleanField(default=False)),
                ('vaginosis_bacteriana', models.BooleanField(default=False)),
                ('flora_anormal', models.BooleanField(default=False)),
                ('actinomyces', models.BooleanField(default=False)),
                ('nega_les_intraepi_malig', models.BooleanField(default=False, help_text='Negativo para Lesión intraepitelial o malignidad')),
                ('camb_react_secu', models.BooleanField(default=False, help_text='Cambios Reactivos Secundarios')),
                ('reparacion', models.BooleanField(default=False)),
                ('inflamacion', models.BooleanField(default=False)),
                ('atrofia', models.BooleanField(default=False)),
                ('diu', models.BooleanField(default=False)),
                ('otro', models.BooleanField(default=False)),
                ('camb_ind_papiloma', models.BooleanField(default=False, help_text='Cambios inducidos por papiloma')),
                ('anor_epi_esca_nat_ind', models.BooleanField(default=False, help_text='Anormalidad del Epitelio Escamoso de naturaleza indeterminada')),
                ('nci_i', models.BooleanField(default=False, help_text='Lesión escamosa intraepitelial de bajo grado (displasia leve NIC. I)')),
                ('les_esc_intr_alto_grado', models.BooleanField(default=False, help_text='Lesión escamosa intraepitelial de alto grado')),
                ('nci_ii', models.BooleanField(default=False, help_text='(Displacia moderada NIC II)')),
                ('nci_iii', models.BooleanField(default=False, help_text='(Displacia severa /Carcinoma in situ NIC III)')),
                ('carc_esca_inv', models.BooleanField(default=False, help_text='Carcinoma escamocelular invasivo')),
                ('anor_epi_glan_nat_inde', models.BooleanField(default=False, help_text='Anomalidades del epitelio glandular de naturaleza indeterminada')),
                ('adenocarcinoma', models.BooleanField(default=False, help_text='Adenocarcinoma')),
                ('orden_examen', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mi_citologia', to='ordenes.OrdenExamen')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]