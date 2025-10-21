from django.db import models

# Create your models here.
# app_editoriales/models.py

from django.db import models

class Empleado(models.Model):
    # editorialID será el 'id' automático de Django (pk)
    nombre = models.CharField(max_length=150, unique=True) # NombreEditorial
    direccion = models.CharField(max_length=200, blank=True, null=True) # Direccion
    telefono = models.CharField(max_length=20, blank=True, null=True) # Telefono
    email = models.EmailField(max_length=100, blank=True, null=True) # EmailContacto
    pais_origen = models.CharField(max_length=100, blank=True, null=True) # PaisOrigen

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['nombre'] # Ordenar por nombre