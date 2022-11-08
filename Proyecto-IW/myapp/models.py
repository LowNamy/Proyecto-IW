from django.db import models

class Genero(models.Model):
    nomGenero = models.CharField(max_length=50)
    descripción = models.CharField(max_length=500)
    def __str__(self):
        return self.nomGenero

class Disco(models.Model):
    nomDisco = models.CharField(max_length = 50)
    fecha = models.CharField(max_length = 50)
    imDisco = models.ImageField()
    def __str__(self):
        return self.nomDisco

class Artistas(models.Model):
    nombre = models.CharField(max_length=50)
    lugarNac = models.CharField(max_length=50)
    imagenArtista = models.ImageField()
    discos = models.ManyToManyField(Disco)
    genero = models.ManyToManyField(Genero)
    def __str__(self):
        return self.nombre

class Grupos(models.Model):
    nomGrupo = models.CharField(max_length=50)
    integrantes = models.CharField(max_length=100)
    lugarNac = models.CharField(max_length=50)
    imagenGrupo = models.ImageField()
    discos = models.ManyToManyField(Disco)
    genero = models.ManyToManyField(Genero)
    def __str__(self):
        return self.nomGrupo
