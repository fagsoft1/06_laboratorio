from django.contrib import admin

from .models import Orden


class OrdenAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'tipo_pago', 'remitente', 'entidad']


admin.site.register(Orden, OrdenAdmin)