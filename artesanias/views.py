from django.shortcuts import render, redirect
from django.contrib import messages
from registros.models import Producto, Municipio, MensajeContacto

def Principal(request):
    return render(request, 'artesanias/principal.html')

def Conocenos(request):
    return render(request, 'artesanias/conocenos.html')

def Catalogo(request):
    # 1. Obtener el valor del parámetro GET 'municipio' desde la URL (?municipio=ID)
    municipio_id = request.GET.get('municipio')
    
    # 2. Base del QuerySet: Todos los productos
    productos = Producto.objects.all()
    
    # 3. Aplicar el filtro si se seleccionó un municipio válido
    if municipio_id and municipio_id.isdigit():
        productos = productos.filter(origen_id=municipio_id)
        
    # 4. Obtener la lista de municipios para construir el menú <select> dinámico
    municipios = Municipio.objects.all().order_by('nombre')
    
    # 5. Preparar el contexto a enviar al Template
    context = {
        'productos': productos,
        'municipios': municipios,
        # Convertimos a entero para poder compararlo en el template y marcarlo como 'selected'
        'municipio_seleccionado': int(municipio_id) if municipio_id and municipio_id.isdigit() else None,
    }
    
    return render(request, 'artesanias/catalogo.html', context)

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

def DetalleProducto(request):
    return render(request, 'artesanias/detalleProducto.html')

def Registro(request):
    return render(request, 'artesanias/registro.html')

def Login(request):
    return render(request, 'artesanias/login.html')
