from rest_framework.serializers import ModelSerializer
from .models import AirPort, AirPlane

class AirportsSerializer(ModelSerializer):
    class Meta:
        model = AirPort
        fields = '__all__'

class AirplanesSerializer(ModelSerializer):
    class Meta:
        model = AirPlane
        fields = '__all__'