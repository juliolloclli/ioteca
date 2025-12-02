# ioteca/ioteca_api/catalogo/views.py

from django.shortcuts import render

# Esta función es la que se ejecuta cuando la URL raíz la llama.
def index(request):
    # Busca 'index.html' dentro de la carpeta 'catalogo/templates/'
    return render(request, 'index.html', {})