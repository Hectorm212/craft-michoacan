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

from artesanias import views as artesanias_views
from usuarios import views as usuarios_views
from pedidos import views as pedidos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # App Artesanias (Catálogo y vistas informativas)
    path('', artesanias_views.Principal, name="Principal"),
    path('conocenos/', artesanias_views.Conocenos, name="Conocenos"),
    path('catalogo/', artesanias_views.Catalogo, name="Catalogo"),
    path('contacto/', artesanias_views.Contacto, name="Contacto"),
    path('detalleProducto/<int:producto_id>/', artesanias_views.DetalleProducto, name="detalleProducto"),

    # App Usuarios (Registro e inicio de sesión)
    path('registro/', usuarios_views.Registro, name="Registro"),
    path('login/', usuarios_views.Login, name="Login"),

    # App Pedidos (Carrito y Checkout)
    path('carrito/', pedidos_views.ver_carrito, name="ver_carrito"),
    path('carrito/agregar/<int:producto_id>/', pedidos_views.agregar_al_carrito, name="agregar_al_carrito"),
    path('carrito/eliminar/<int:item_id>/', pedidos_views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path('carrito/procesar/', pedidos_views.procesar_compra, name="procesar_compra"),
    path('compra-exitosa/<int:pedido_id>/', pedidos_views.compra_exitosa, name="compra_exitosa"),
    path('mis-pedidos/', pedidos_views.mis_pedidos, name="mis_pedidos"),

    path('logout/', usuarios_views.Logout, name="Logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
