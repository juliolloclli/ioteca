from django.db import models

class Catalogo(models.Model):
    """Model definition for Catalogo."""

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=60, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'

    def __str__(self):
        return self.nombre


