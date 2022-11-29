from unittest import loader
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Artistas, Disco, Genero


def index(request):
    generos = Genero.objects.order_by('nomGenero')
    context = {'lista_generos': generos }
    return render(request, 'index.html', context)

def lista_artistas(request):
    artistas = Artistas.objects.order_by('nombre')
    context = {'lista_artistas': artistas}
    return render(request, 'lista_artistas.html', context)

def lista_discos(request):
    disco = Disco.objects.order_by('nomDisco')
    context = {'lista_discos': disco}
    return render(request, 'lista_discos.html', context)

#devuelve los detalles de un artista
def artista(request, artista_id):
    artista = get_object_or_404(Artistas, pk=artista_id)
    context = { 'artista': artista }
    return render(request, 'artistas.html', context)

def formulario(request):
    return render(request, 'formulario.html')