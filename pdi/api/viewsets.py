from ..models import Pdi
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PdiSerializers

class PdiViewSet(viewsets.ModelViewSet):
    queryset = Pdi.objects.all()
    serializer_class = PdiSerializers
    permission_classes = [permissions.IsAuthenticated]