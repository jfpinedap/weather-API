"""
Weather Serializers
"""

# Libreries
from rest_framework.serializers import ModelSerializer

# Models
from .models import Weather


class WeatherSerializer(ModelSerializer):
    """Serializer for data Weather"""

    class Meta:
        model = Weather
        exclude = ['id']