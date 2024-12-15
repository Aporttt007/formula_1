from rest_framework import viewsets
from .models import Circuit
from .serializers import CircuitSerializer

class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
