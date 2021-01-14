"""
Weather Serializers
"""

# Libreries
from rest_framework.serializers import ModelSerializer

# Models
from . import models


class WeatherSerializer(ModelSerializer):
    """Serializer for data Weather"""

    class Meta:
        model = models.Weather
        exclude = ['id']


class ForecastSerializer(ModelSerializer):
    """Serializer for data Forecast"""

    class Meta:
        model = models.Forecast
        exclude = ['id']