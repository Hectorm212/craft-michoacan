from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from artesanias.models import Producto
from .models import Carrito, ItemCarrito, Pedido, DetallePedido

@login_required(login_url='Login')
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1)) if request.method == 'POST' else 1
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not item_creado:
        item.cantidad += cantidad
        item.save()
        messages.success(request, f'Se añadieron {cantidad} unidad(es) más de "{producto.nombre}" a tu carrito.')
    else:
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
    
    if not items:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('ver_carrito')
    
    pedido = Pedido.objects.create(
        usuario=request.user,
        total=carrito.total(),
        estado='pagado',
        direccion_envio="Dirección registrada",
        telefono="4430000000"
    )
    
    for item in items:
        DetallePedido.objects.create(
            pedido=pedido,
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio
        )
    
    items.delete()
    return redirect('compra_exitosa', pedido_id=pedido.id)

@login_required(login_url='Login')
def compra_exitosa(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    return render(request, 'artesanias/compra_exitosa.html', {'pedido': pedido})

@login_required(login_url='Login')
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'artesanias/mis_pedidos.html', {'pedidos': pedidos})