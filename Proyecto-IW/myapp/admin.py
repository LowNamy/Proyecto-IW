from django.contrib import admin
from .models import Disco, Artistas, Genero

admin.site.register(Artistas)
admin.site.register(Disco)
admin.site.register(Genero)
