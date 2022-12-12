from django.contrib import admin
from .models import Disco, Artistas, Genero

class DiscoAdmin(admin.ModelAdmin):
    list_display = ["nomDisco", "lanzamiento"]
    list_editable = ["lanzamiento"]
    search_fields = ["nomDisco"]
    list_filter = ["lanzamiento"]
    list_per_page = 5

class LinkAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return('key', 'name')
        else:
            return()

admin.site.register(Artistas)
admin.site.register(Disco, DiscoAdmin)
admin.site.register(Genero)
