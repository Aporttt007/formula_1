from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SponsorViewSet, TeamViewSet, DriverViewSet, CarViewSet

router = DefaultRouter()
router.register(r'sponsors', SponsorViewSet, basename='sponsor')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'drivers', DriverViewSet, basename='driver')
router.register(r'cars', CarViewSet, basename='car')

urlpatterns = [
    path('', include(router.urls)),
]
