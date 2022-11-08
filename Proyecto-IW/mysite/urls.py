"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from myapp import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('lista_generos', views.lista_generos, name='lista_generos'),
    path('lista_artistas', views.lista_artistas, name='lista_artistas'),
    path('lista_grupos', views.lista_grupos, name='lista_grupos'),
    path('lista_discos', views.lista_discos, name='lista_discos'),
    
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]
