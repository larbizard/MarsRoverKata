from rest_framework import serializers
from models import Rover


class RoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rover
        fiels = '__all__'