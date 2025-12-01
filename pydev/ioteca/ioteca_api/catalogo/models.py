from django.db import models

# Create your models here.

class Catalogo(models.Model):
    """Model definition for Catalogo."""
    
    # TODO: Define fields here

    nombre = models.CharField(max_length=60)
    codigo =models.CharField(max_length=60, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
     """Model definition for Catalogo."""
     verbose_name = 'Catalogo'
     verbose_name_plural = 'Catalogos'

    def __str__(self):
        """Unicode representation of Catalogo."""
        return self.nombre