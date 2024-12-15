from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Подключаем маршруты каждого приложения
    path('api/circuits/', include('circuits.urls')),
    path('api/teams/', include('teams.urls')),
    path('api/races/', include('races.urls')),
    path('api/history/', include('history.urls')),
    path('api/fanservice/', include('fanservice.urls')),
    path('api/events/', include('events.urls')),
]
