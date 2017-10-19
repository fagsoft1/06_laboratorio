from django.db import models
from model_utils.models import TimeStampedModel

from pacientes.models import Paciente
from medicos.models import MedicoRemitente
from entidades.models import Entidad


class Orden(TimeStampedModel):
    RELACION_COBRO_CHOICES = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('relacion_cobro', 'Relación de Cobro'),
        ('cortesia', 'Cortesía'),
    )
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='mis_ordenes')
    tipo_pago = models.CharField(max_length=30, choices=RELACION_COBRO_CHOICES, default='efectivo')
    remitente = models.ForeignKey(MedicoRemitente, on_delete=models.PROTECT, related_name='mis_ordenes')
    entidad = models.ForeignKey(Entidad, on_delete=models.PROTECT, related_name='mis_ordenes')
    nombre_contacto_alternativo = models.CharField(max_length=200, verbose_name='Nombre Contacto')
    numero_contacto_alternativo = models.CharField(max_length=100, verbose_name='Número Contacto')
    direccion_contacto_alternativo = models.CharField(max_length=200, verbose_name='Dirección Contacto')