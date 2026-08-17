from django.contrib import admin

from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre_completo', 'ciudad', 'cp')
    search_fields = ('nombre_completo', 'usuario__username', 'usuario__email', 'ciudad')