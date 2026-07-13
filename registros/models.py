from django.db import models

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
    nombre = models.CharField(max_length=150, verbose_name="Nombre completo")
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
