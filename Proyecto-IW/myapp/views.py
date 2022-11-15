from unittest import loader
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Artistas, Disco, Genero, Grupos


def index(request):
    generos = Genero.objects.order_by('nomGenero')
    context = {'lista_generos': generos }
    return render(request, 'index.html', context)

def lista_artistas(request):
    artistas = Artistas.objects.order_by('nombre')
    context = {'lista_artistas': artistas}
    return render(request, 'lista_artistas.html', context)

def lista_grupos(request):
    grupos = Grupos.objects.order_by('nomGrupo')
    context = {'lista_grupos': grupos}
    return render(request, 'lista_grupos.html', context)

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

#Devuelve los grupos de un genero o disco
def grupoG(request, genero_id):
	genero = get_object_or_404(Genero, pk=genero_id)
	grupo =  genero.grupo_set.all()
	context = {'genero': genero, 'grupo' : grupo }
	return render(request, 'grupos.html', context)

def grupoD(request, disco_id):
	discos = get_object_or_404(Disco, pk=disco_id)
	grupo =  discos.grupo_set.all()
	context = { 'grupo' : grupo, 'discos': discos }
	return render(request, 'grupos.html', context)

#devuelve los detalles de un artista y grupo
def artista(request, artista_id):
    artista = get_object_or_404(Artistas, pk=artista_id)
    genero =  artista.genero.all()
    discos =  artista.discos.all()
    context = { 'artista': artista, 'genero' : genero, 'discos' : discos }
    return render(request, 'artistas.html', context)

def grupo(request, grupo_id):
    grupo = get_object_or_404(Grupos, pk=grupo_id)
    genero =  grupo.genero.all()
    discos =  grupo.discos.all()
    context = { 'grupo': grupo, 'genero' : genero, 'discos' : discos }
    return render(request, 'grupos.html', context)
