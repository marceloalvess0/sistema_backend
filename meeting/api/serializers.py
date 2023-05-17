from ..models import Meeting
from rest_framework import serializers

class MeetingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = ['title','collaborator','datetime','details','url_meeting']
