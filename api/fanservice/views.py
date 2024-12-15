from rest_framework import viewsets
from .models import User, Merchandise
from .serializers import UserSerializer, MerchandiseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer
