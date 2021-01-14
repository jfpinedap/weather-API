"""Weather models"""

# Libraries
from django.db import models

# Utils
from .utils import get_wind, get_hour, get_date


class Weather(models.Model):
    """
    Weather Model
    Defines the attributes of a weather
    """
    location_name = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    wind = models.CharField(max_length=255)
    cloudiness = models.CharField(max_length=255)
    pressure = models.CharField(max_length=255)
    humidity = models.CharField(max_length=255)
    sunrise = models.CharField(max_length=255)
    sunset = models.CharField(max_length=255)
    geo_coordinates = models.CharField(max_length=255)
    requested_time = models.CharField(max_length=255)
    forecast = models.JSONField()

    def __init__(self, *args, **kwargs):
        """
        Init method is used to extract data from OpenWeather response
        and transform to required Weather model.
        """
        kwargs = self.__extract_transform(**kwargs)
        super().__init__(*args, **kwargs)

    def __extract_transform(self, **kwargs):
        sys = kwargs.get('sys', {})
        main = kwargs.get('main', {})
        timezone = kwargs.get('timezone', 0)
        coord = kwargs.get('coord', {})
        return {
            'location_name': '{0}, {1}'.format(
                kwargs.get('name', ''),
                sys.get('country', '')
            ),
            'temperature': '{0} °C'.format(
                main.get('temp', '')
            ),
            'wind': get_wind(
                wind=kwargs.get('wind', '')
            ),
            'cloudiness': kwargs.get(
                'weather', [{}])[0].get('description', ''
            ).capitalize(),
            'pressure': '{} hpa'.format(
                main.get('pressure', '')
            ),
            'humidity': '{}%'.format(
                main.get('humidity', '')
            ),
            'sunrise': get_hour(
                utc_time=sys.get('sunrise', 0),
                timezone=timezone
            ),
            'sunset': get_hour(
                utc_time=sys.get('sunset', 0),
                timezone=timezone
            ),
            'geo_coordinates': '[{}, {}]'.format(
                round(coord.get('lat', 0), 2),
                round(coord.get('lon', 0), 2)
            ),
            'requested_time': get_date(
                utc_time=kwargs.get('dt', 0),
                timezone=timezone
            )
        }

    def save(self, *args, **kwargs):
        """
        Override the model's save method to prevent saving to the database
        """
        pass

    class Meta:
        managed = False
