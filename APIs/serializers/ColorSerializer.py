from rest_framework import serializers
from APIs.models import Colours




class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = ["colourName"]