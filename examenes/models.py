from django.db import models


class CupsGrupo(models.Model):
    nombre = models.CharField(max_length=200)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cups Grupo'
        verbose_name_plural = 'Cups Grupos'


class CupsSubGrupo(models.Model):
    nombre = models.CharField(max_length=200)
    grupo = models.ForeignKey(CupsGrupo, related_name='mis_subgrupos', on_delete=models.PROTECT)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cups Sub Grupo'
        verbose_name_plural = 'Cups Sub Grupos'


class Examen(models.Model):
    subgrupo_cups = models.ForeignKey(CupsSubGrupo, related_name="mis_examenes", null=True, blank=True,
                                      on_delete=models.PROTECT)
    codigo_cups = models.PositiveIntegerField(help_text='Código de clasificación única en procedimientos en salud',
                                              unique=True)
    nombre = models.CharField(verbose_name='Nombre del Examen', max_length=300)
    nombre_corto = models.CharField(verbose_name='Nombre del Examen (Corto)', max_length=100, blank=True, null=True)
    valor_referencia = models.TextField(verbose_name='Valor de Referencia', blank=True, null=True)
    unidad_medida = models.CharField(max_length=50, verbose_name='Unidad de Medida', blank=True, null=True)
    tecnica = models.CharField(max_length=100, verbose_name='Técnica', blank=True, null=True)
    costo_referencia = models.DecimalField(max_digits=10, decimal_places=1, default=0,
                                           verbose_name='Costo Referencia del Examen')
    multifirma = models.BooleanField(default=False, verbose_name='Multiple Firma')
    especial = models.BooleanField(default=False, verbose_name='Plantilla Especial')
    nro_plantilla = models.PositiveIntegerField(verbose_name='Nro. Plantilla Especial', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Exámen'
        verbose_name_plural = 'Examenes'
