"""
View of Weather
"""

# Libraries
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse

# Models
from .models import Weather

# Serializers
from . import serializers

# Utils
from .utils import weather_request

class WeatherView(APIView):
    """
    Weather View
    Perform weather data from OpenWeather using city and country
    """
    model = Weather
    serializer = serializers.WeatherSerializer

    def get(self, request):
        city = request.GET.get('city', None)
        country = request.GET.get('country', None)

        # Get weather data from OpenWeather
        response = weather_request(city=city, country=country)

        weather = None
        if response.get('cod', 404) == 200:
            weather = Weather(**response)
        else:
            return JsonResponse(response)

        serializer = self.serializer(weather)

        return Response({
            'Response': serializer.data
        })
        