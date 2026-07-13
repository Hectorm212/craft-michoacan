from django.contrib import admin
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
    # Columnas que se mostrarán en la lista principal del admin
    list_display = ('nombre', 'categoria', 'origen', 'precio', 'stock')
    
    # Filtros laterales
    list_filter = ('categoria', 'origen')
    
    # Barra de búsqueda (busca por nombre de producto y cruza a las tablas relacionadas)
    search_fields = ('nombre', 'categoria__nombre', 'origen__nombre')
    
    # Campos que se pueden editar directamente desde la lista sin entrar al detalle
    list_editable = ('precio', 'stock')

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'nombre', 'email', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto')
    actions = ["marcar_como_leido", "marcar_como_no_leido"] #SE agrega una accion personalizada para marcar mensajes como leídos o no leídos

    # Acciones personalizadas para marcar mensajes como leídos o no leídos
    @admin.action(description='Marcar mensajes seleccionados como LEIDOS')
    def marcar_como_leido(self, request, queryset):
        filas_actualizadas = queryset.update(leido=True) #Segun las casillas seleccionazadas, se actualiza el campo Leido a True (leido) o false (no leido)
        self.message_user(
            request,
            f'Se actualizaron {filas_actualizadas} mensajes como leidos correctamente' #por ultimo al guardar los cambios, se muestra un mensaje de confirmacion para el usuario admin
        )

    @admin.action(description='Marcar mensajes seleccionados como No LEIDOS')
    def marcar_como_no_leido(self, request, queryset):
        filas_actualizadas = queryset.update(leido=False)
        self.message_user(
            request,
            f'Se actualizaron {filas_actualizadas} mensajes como no leidos correctamente'
        )



