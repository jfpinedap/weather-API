"""
View of Weather
"""

# Libraries
from django.http import JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


# Models
from . import models

# Serializers
from . import serializers

# Utils
from .utils import weather_request, forecast_request


class WeatherView(APIView):
    """
    Weather View
    Perform weather data from OpenWeather using city and country
    """
    model = models.Weather
    serializer = serializers.WeatherSerializer

    def get(self, request):
        city = request.GET.get('city', None)
        country = request.GET.get('country', None)

        # Get weather data from OpenWeather
        response = weather_request(city=city, country=country)
        coord = response.get('coord', {})
        lon = coord.get('lon', 0)
        lat = coord.get('lat', 0)

        weather = None
        if response.get('cod', 404) == 200:
            weather = models.Weather(**response)
        else:
            return JsonResponse(response)

        # Get forecast from OpenWeather
        forecast_response = forecast_request(lat=lat, lon=lon)
        timezone_offset = forecast_response.get('timezone_offset', 0)
        daily = forecast_response.get('daily', [])
        forecast = [
            dict(serializers.ForecastSerializer(
                models.Forecast(timezone_offset, **day)
            ).data)
            for day in daily
        ]

        # Complement Weather Data with forecast and serialize
        weather.forecast = forecast
        serializer = self.serializer(weather)

        return Response({
            'Response': serializer.data
        })
        