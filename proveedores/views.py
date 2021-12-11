from rest_framework import viewsets
from .models import *
from .serializer import *

# Create your views here.
class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializers
