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

#devuelve los artistas de un genero o discos
def artistasG(request, genero_id):
	genero = get_object_or_404(Genero, pk=genero_id)
	artistas =  genero.artistas_set.all()
	context = {'genero': genero, 'artistas' : artistas }
	return render(request, 'artistas.html', context)

def artistasD(request, disco_id):
	discos = get_object_or_404(Disco, pk=disco_id)
	artistas =  discos.artistas_set.all()
	context = { 'artistas' : artistas, 'discos': discos }
	return render(request, 'artistas.html', context)

#devuelve los detalles de un artista y grupo
def artista(request, artista_id):
    artista = get_object_or_404(Artistas, pk=artista_id)
    genero =  artista.genero.all()
    discos =  artista.discos.all()
    context = { 'artista': artista, 'genero' : genero, 'discos' : discos }
    return render(request, 'artistas.html', context)
