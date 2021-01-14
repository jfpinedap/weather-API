"""Weather tests"""

# Libraries
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from .models import Weather, Forecast

# Serializers
from . import serializers

# Utils
from .utils import (
    degrees_to_cardinal, beaufort_label
)

# Data
from .test_data import (
    weather_data, forecast_data,
    expected_weather, expected_forecast,
    beaufort_labels, deg_directions
)


class WeatherTestCase(APITestCase):

    def test_get_valid_weather(self):
        """
        Ensure that request to OpenWeather and get a response 200 OK.
        """
        url = '/weather?city=bogota&country=co'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_weather(self):
        """
        Ensure that request to OpenWeather and get a response 404 not found
        """
        url = '/weather?city=zzzz&country=co'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_weather_model(self):
        """
        Ensure that Weather Model and serializer works as expected.
        """
        weather = Weather(**weather_data)
        weather = serializers.WeatherSerializer(weather).data
        self.assertEqual(dict(weather), expected_weather)

    def test_forecast_model(self):
        """
        Ensure that Forecast Model and serializer works as expected.
        """
        forecast = Forecast(timezone_offset=-18000, **forecast_data)
        forecast = serializers.ForecastSerializer(forecast).data
        self.assertEqual(dict(forecast), expected_forecast)

    def test_degrees_to_cardinal_function(self):
        """
        Ensure that conversion from degrees to cardinal/intercardinal direction
        works as expected.
        """
        for deg, direction in deg_directions.items():
            self.assertEqual(
                degrees_to_cardinal(deg=deg),
                direction
            )

    def test_beaufort_label_function(self):
        """
        Ensure that Beaufort labeling works as expected.
        """
        for wind_speed, label in beaufort_labels.items():
            self.assertEqual(
                beaufort_label(wind_speed=wind_speed),
                label
            )
