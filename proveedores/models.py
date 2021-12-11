from django.db import models

# Create your models here.
class Proveedores(models.Model):
    Nit = models.IntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=255, null=True)
    direccion_proveedor = models.CharField(max_length=255, null=True)
    telefono_proveedor = models.CharField(max_length=255, null=True)
    ciudad_proveedor = models.CharField(max_length=255, null=True)
