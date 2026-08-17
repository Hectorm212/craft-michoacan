from django.contrib import admin

# Personalización del panel administrativo
admin.site.site_header = "Panel de Control - Craft Mich"
admin.site.site_title = "Craft Mich Admin"
admin.site.index_title = "Administración del Sistema"

from .models import Categoria, Municipio, Producto, MensajeContacto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'origen', 'precio', 'stock')
    list_filter = ('categoria', 'origen')
    search_fields = ('nombre', 'categoria__nombre', 'origen__nombre')
    list_editable = ('precio', 'stock')

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'nombre', 'email', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto')
    actions = ["marcar_como_leido", "marcar_como_no_leido"]

    @admin.action(description='Marcar mensajes seleccionados como LEÍDOS')
    def marcar_como_leido(self, request, queryset):
        filas_actualizadas = queryset.update(leido=True)
        self.message_user(
            request,
            f'Se actualizaron {filas_actualizadas} mensajes como leídos correctamente'
        )

    @admin.action(description='Marcar mensajes seleccionados como NO LEÍDOS')
    def marcar_como_no_leido(self, request, queryset):
        filas_actualizadas = queryset.update(leido=False)
        self.message_user(
            request,
            f'Se actualizaron {filas_actualizadas} mensajes como no leídos correctamente'
        )

# Inyección forzada de estilos CSS para todo el Admin
class AdminStyleMedia:
    css = {
        'all': ('artesanias/css/admin_custom.css',)
    }

admin.site.site_header = "Panel de Control - Craft Mich"