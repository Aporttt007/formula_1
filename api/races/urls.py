from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RaceViewSet, RaceResultViewSet, PitStopViewSet, SessionTimingViewSet

router = DefaultRouter()
router.register(r'races', RaceViewSet, basename='race')
router.register(r'race-results', RaceResultViewSet, basename='race_result')
router.register(r'pit-stops', PitStopViewSet, basename='pit_stop')
router.register(r'session-timings', SessionTimingViewSet, basename='session_timing')

urlpatterns = [
    path('', include(router.urls)),
]
