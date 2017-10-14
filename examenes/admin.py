from django.contrib import admin

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin

from .models import Examen


class ExamenResource(ModelResource):
    class Meta:
        model = Examen


class ExamenAdmin(ImportExportModelAdmin):
    list_display = ['codigo_cups', 'nombre', 'nombre_corto', 'valor_referencia', 'unidad_medida', 'tecnica']
    search_fields = ['codigo_cups', 'nombre']
    resource_class = ExamenResource


admin.site.register(Examen, ExamenAdmin)