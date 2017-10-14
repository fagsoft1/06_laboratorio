from django.db import models
from model_utils.models import TimeStampedModel


class Paciente(TimeStampedModel):
    nombre = models.CharField(max_length=60)
    nombre_segundo = models.CharField(max_length=60, null=True, blank=True)
    apellido = models.CharField(max_length=60)
    apellido_segundo = models.CharField(max_length=60, null=True, blank=True)
    fecha_nacimiento = models.DateTimeField()
    telefono = models.CharField(max_length=20, null=True, blank=True)
    telefono_2 = models.CharField(max_length=20, null=True, blank=True)
    telefono_3 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    email_2 = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Pacientes'
        verbose_name = 'Paciente'

    def __str__(self):
        return '%s %s %s %s' % (self.nombre, self.nombre_segundo, self.apellido, self.apellido_segundo)
