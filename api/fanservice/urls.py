from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MerchandiseViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'merchandise', MerchandiseViewSet, basename='merchandise')

urlpatterns = [
    path('', include(router.urls)),
]
