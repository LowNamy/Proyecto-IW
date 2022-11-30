from django.contrib import admin
from django.urls import include, path
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('lista_generos', views.index, name='lista_generos'),
    path('lista_artistas', views.lista_artistas, name='lista_artistas'),
    path('lista_discos', views.lista_discos, name='lista_discos'),
    path('artista/<int:artista_id>', views.artista, name='artista'),
    path('disco/<int:disco_id>', views.disco, name='disco'),

    path('formulario', views.formulario),

    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]

urlpatterns += staticfiles_urlpatterns()
