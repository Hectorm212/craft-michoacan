"""
URL configuration for craftMich project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from artesanias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Principal, name="Principal"),
    path('conocenos/', views.Conocenos, name="Conocenos"),
    path('catalogo/', views.Catalogo, name="Catalogo"),
    path('contacto/', views.Contacto, name="Contacto"),
    path('registro/', views.Registro, name="Registro"),
    path('login/', views.Login, name="Login"),
    # Rutas del Carrito de Compras
    path('carrito/', views.ver_carrito, name="ver_carrito"),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name="agregar_al_carrito"),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path('detalleProducto/<int:producto_id>/', views.DetalleProducto, name="detalleProducto"),
    # Checkout de compra
    path('carrito/procesar/', views.procesar_compra, name="procesar_compra"),
    path('compra-exitosa/<int:pedido_id>/', views.compra_exitosa, name="compra_exitosa"),
    path('mis-pedidos/', views.mis_pedidos, name="mis_pedidos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
