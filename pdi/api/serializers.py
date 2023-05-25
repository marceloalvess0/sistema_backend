from ..models import Pdi
from rest_framework import serializers

class PdiSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pdi
        fields = ['objective_title','developed_areas','initial_datetime','final_datetime','reference_url','file','description']
