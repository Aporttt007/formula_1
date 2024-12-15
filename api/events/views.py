from rest_framework import viewsets
from .models import Ticket, MediaCoverage, LiveStream
from .serializers import TicketSerializer, MediaCoverageSerializer, LiveStreamSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class MediaCoverageViewSet(viewsets.ModelViewSet):
    queryset = MediaCoverage.objects.all()
    serializer_class = MediaCoverageSerializer

class LiveStreamViewSet(viewsets.ModelViewSet):
    queryset = LiveStream.objects.all()
    serializer_class = LiveStreamSerializer
