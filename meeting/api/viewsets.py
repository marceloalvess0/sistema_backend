from ..models import Meeting
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MeetingSerializers

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializers
    permission_classes = [permissions.IsAuthenticated]