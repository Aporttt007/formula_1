from rest_framework import viewsets
from .models import Race, RaceResult, PitStop, SessionTiming
from .serializers import RaceSerializer, RaceResultSerializer, PitStopSerializer, SessionTimingSerializer

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceResultViewSet(viewsets.ModelViewSet):
    queryset = RaceResult.objects.all()
    serializer_class = RaceResultSerializer

class PitStopViewSet(viewsets.ModelViewSet):
    queryset = PitStop.objects.all()
    serializer_class = PitStopSerializer

class SessionTimingViewSet(viewsets.ModelViewSet):
    queryset = SessionTiming.objects.all()
    serializer_class = SessionTimingSerializer
