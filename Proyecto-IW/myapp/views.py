from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Genero, Artistas, Grupos, Disco

def index(request):
    generos = Genero.objects.order_by('nomGenero')
    context = {'lista_generos': generos }
    return render(request, 'index.html', context)

def lista_artistas(request):
    artistas = Artistas.objects.order_by('nombre')
    context = {'artistas': artistas}
    return render(request, 'lista_artistas.html', context)