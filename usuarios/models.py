from django.db import models

from django.conf import settings

class Perfil(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil', verbose_name="Usuario")
    nombre_completo = models.CharField(max_length=200, verbose_name="Nombre completo")
    domicilio = models.CharField(max_length=255, verbose_name="Domicilio (Calle, número, colonia)")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    cp = models.CharField(max_length=5, verbose_name="Código Postal")

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuarios"

    def __str__(self):
        return f"{self.nombre_completo} ({self.usuario.email})"