# catalogo/admin.py

from django.contrib import admin
from .models import Catalogo # Asegúrate de que importas el modelo correcto

# 1. Renombra la clase a CatalogoAdmin para ser clara
class CatalogoAdmin(admin.ModelAdmin):
    # Combina los campos de list_display y ajusta list_per_page y search_fields.
    # Usaremos los campos que te dan la búsqueda y la paginación que deseas:
    
    # Define qué campos se muestran en la tabla del administrador
    list_display = ('nombre', 'codigo', 'estado', 'id') 
    
    # Paginación: Mostrar 2 elementos por página
    list_per_page = 2
    
    # Búsqueda: Buscar en los campos 'nombre' y 'codigo'
    search_fields = ('nombre', 'codigo') 
    
    # NOTA: Quité 'categoria' del list_display porque no es un campo directo de Catalogo
    # a menos que lo hayas definido. Si es un campo, puedes añadirlo aquí.

# 2. Registra el modelo usando la clase de configuración
admin.site.register(Catalogo, CatalogoAdmin)