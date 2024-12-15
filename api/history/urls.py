from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoryAchievementsViewSet

router = DefaultRouter()
router.register(r'history-achievements', HistoryAchievementsViewSet, basename='history_achievements')

urlpatterns = [
    path('', include(router.urls)),
]
