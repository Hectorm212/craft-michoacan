from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producto, Municipio, MensajeContacto, Categoria

def Principal(request):
    return render(request, 'artesanias/principal.html')

def Conocenos(request):
    return render(request, 'artesanias/conocenos.html')

def Catalogo(request):
    # 1. Obtener parámetros GET de la URL
    municipio_id = request.GET.get('municipio')
    categoria_id = request.GET.get('categoria')
    
    # 2. Base del QuerySet
    productos = Producto.objects.all()
    
    # 3. Aplicar filtros combinados
    if municipio_id and municipio_id.isdigit():
        productos = productos.filter(origen_id=municipio_id)
        
    if categoria_id and categoria_id.isdigit():
        productos = productos.filter(categoria_id=categoria_id)
        
    # 4. Obtener listas para los menús <select>
    municipios = Municipio.objects.all().order_by('nombre')
    categorias = Categoria.objects.all().order_by('nombre')
    
    # 5. Contexto enviado a la plantilla
    context = {
        'productos': productos,
        'municipios': municipios,
        'categorias': categorias,
        'municipio_seleccionado': int(municipio_id) if municipio_id and municipio_id.isdigit() else None,
        'categoria_seleccionada': int(categoria_id) if categoria_id and categoria_id.isdigit() else None,
    }
    
    return render(request, 'artesanias/catalogo.html', context)

@login_required(login_url='Login')
def Contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        
        if nombre and email and asunto and mensaje:
            MensajeContacto.objects.create(
                nombre=nombre,
                email=email,
                asunto=asunto,
                mensaje=mensaje
            )
            messages.success(request, '¡Gracias por contactarnos! Hemos recibido tu mensaje y te responderemos pronto.')
            return redirect('Contacto')
            
    return render(request, 'artesanias/contacto.html')

@login_required(login_url='Login')
def DetalleProducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'artesanias/detalleProducto.html', {'producto': producto})