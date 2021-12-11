from rest_framework import serializers
from .models import *

class ProveedoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['Nit', 'nombre_proveedor', 'direccion_proveedor', 'telefono_proveedor', 'ciudad_proveedor']
