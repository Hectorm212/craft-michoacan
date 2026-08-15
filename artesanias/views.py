from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from registros.models import Producto, Municipio, MensajeContacto, Carrito, ItemCarrito,Pedido, DetallePedido

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

def DetalleProducto(request, producto_id):
    # Busca el producto por ID o muestra un error 404 si no existe
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'artesanias/detalleProducto.html', {'producto': producto})

def Registro(request):
    return render(request, 'artesanias/registro.html')

def Login(request):
    return render(request, 'artesanias/login.html')


@login_required(login_url='Login')
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Obtener la cantidad enviada desde el formulario HTML (por defecto 1)
    cantidad = int(request.POST.get('cantidad', 1)) if request.method == 'POST' else 1
    
    # Obtener o crear el carrito del usuario
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    
    # Buscar si el producto ya está en el carrito
    item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not item_creado:
        # Si ya existía, le sumamos la cantidad solicitada
        item.cantidad += cantidad
        item.save()
        messages.success(request, f'Se añadieron {cantidad} unidad(es) más de "{producto.nombre}" a tu carrito.')
    else:
        # Si es la primera vez que entra, le asignamos la cantidad elegida
        item.cantidad = cantidad
        item.save()
        messages.success(request, f'Se agregaron {cantidad} unidad(es) de "{producto.nombre}" a tu carrito.')
        
    return redirect('ver_carrito')

@login_required(login_url='Login')
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    
    context = {
        'carrito': carrito,
        'items': items,
        'total': carrito.total(),
    }
    return render(request, 'artesanias/carrito.html', context)


@login_required(login_url='Login')
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    nombre_producto = item.producto.nombre
    item.delete()
    messages.success(request, f'"{nombre_producto}" fue eliminado del carrito.')
    return redirect('ver_carrito')


@login_required(login_url='Login')
def procesar_compra(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    
    # Si el carrito está vacío, no procesamos nada
    if not items:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('ver_carrito')
    
    # 1. Crear el registro del Pedido
    pedido = Pedido.objects.create(
        usuario=request.user,
        total=carrito.total(),
        estado='pagado',
        direccion_envio="Dirección de prueba (Proyecto Escolar)",
        telefono="4430000000"
    )
    
    # 2. Copiar los items del carrito a DetallePedido
    for item in items:
        DetallePedido.objects.create(
            pedido=pedido,
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio
        )
    
    # 3. Vaciar el carrito de compras
    items.delete()
    
    # 4. Redirigir a la pantalla de éxito mandando el ID del pedido
    return redirect('compra_exitosa', pedido_id=pedido.id)


@login_required(login_url='Login')
def compra_exitosa(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    return render(request, 'artesanias/compra_exitosa.html', {'pedido': pedido})


@login_required(login_url='Login')
def mis_pedidos(request):
    # Obtiene todos los pedidos realizados por el usuario logueado, del más reciente al más antiguo
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'artesanias/mis_pedidos.html', {'pedidos': pedidos})