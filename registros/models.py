from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de Categoría")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Municipio(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Municipio")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    origen = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='productos', verbose_name="Municipio de Origen")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio (MXN)")
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name="Imagen del Producto")
    stock = models.PositiveIntegerField(default=0, verbose_name="Cantidad en Stock")



    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-id'] # Ordenar por los más recientes por defecto


class MensajeContacto(models.Model):
    nombre =  models.CharField(max_length=150, verbose_name="Nombre completo")
    email = models.EmailField(verbose_name="Correo electrónico")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")
    leido = models.BooleanField(default=False, verbose_name="¿Leído?")

    def __str__(self):
        return f"{self.asunto} - {self.nombre}"


    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio']


class Carrito(models.Model):
    # Se relaciona con un usuario registrado
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carrito', verbose_name="Usuario")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Carrito de Compras"
        verbose_name_plural = "Carritos de Compras"

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

    # Método para calcular el total acumulado de la cesta
    def total(self):
        return sum(item.subtotal() for item in self.items.all())


class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items', verbose_name="Carrito")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")

    class Meta:
        verbose_name = "Item del Carrito"
        verbose_name_plural = "Items del Carrito"

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre}"

    # Método para calcular el subtotal de cada línea de producto
    def subtotal(self):
        return self.cantidad * self.producto.precio        


class Pedido(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente de Pago'),
        ('pagado', 'Pagado'),
        ('enviado', 'Enviado'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos', verbose_name="Cliente")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Compra")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Total ($ MXN)")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente', verbose_name="Estado del Pedido")
    
    # Datos para el envío de las artesanías
    direccion_envio = models.TextField(verbose_name="Dirección de Envío")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono de Contacto")
    notas = models.TextField(blank=True, null=True, verbose_name="Notas de la entrega")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles', verbose_name="Pedido")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, verbose_name="Producto")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario ($ MXN)")

    class Meta:
        verbose_name = "Detalle del Pedido"
        verbose_name_plural = "Detalles del Pedido"

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} (Pedido #{self.pedido.id})"

    def subtotal(self):
        return self.cantidad * self.precio_unitario