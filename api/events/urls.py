from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, MediaCoverageViewSet, LiveStreamViewSet

router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'media-coverage', MediaCoverageViewSet, basename='media_coverage')
router.register(r'live-streams', LiveStreamViewSet, basename='live_stream')

urlpatterns = [
    path('', include(router.urls)),
]
