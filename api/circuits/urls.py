from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CircuitViewSet

router = DefaultRouter()
router.register(r'circuits', CircuitViewSet, basename='circuit')

urlpatterns = [
    path('', include(router.urls)),
]
