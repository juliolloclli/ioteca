from django.contrib import admin
from .models import Catalogo

class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nombre", "codigo", "estado")
    search_fields=("nombre", "codigo")
    list_per_page=3

admin.site.register(Catalogo, CategoriaAdmin)
