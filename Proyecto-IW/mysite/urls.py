from django.contrib import admin
from django.urls import include, path
from myapp import views

urlpatterns = [
    path('lista_generos', views.index, name='lista_generos'),
    path('lista_artistas', views.lista_artistas, name='lista_artistas'),
    path('lista_grupos', views.lista_grupos, name='lista_grupos'),
    path('lista_discos', views.lista_discos, name='lista_discos'),
    path('genero/<int:genero_id>/artistas', views.artistasG, name='artistas'),
    path('discos/<int:disco_id>/artistas', views.artistasD, name='artistas'),
    path('genero/<int:genero_id>/grupo', views.grupoG, name='grupo'),
    path('discos/<int:disco_id>/grupo', views.grupoD, name='grupo'),
    path('artista/<int:artista_id>', views.artista, name='artista'),
    path('grupo/<int:grupo_id>', views.grupo, name='grupo'),

    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]
