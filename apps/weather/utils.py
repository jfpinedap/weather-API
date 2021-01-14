"""Utils for Weather"""

# Libraries
import json
import environ
import requests
from time import strftime, gmtime


OPENWEATHER_URL = environ.Env().str(
    'OPENWEATHER_URL',
    'https://api.openweathermap.org'
)


OPENWEATHER_APPID = environ.Env().str(
    'OPENWEATHER_APPID',
    ''
)


def degrees_to_cardinal(deg: int) -> str:
    """
    Transform degress to cardinal or subcardinal direction.
    """
    directions = [
        "north", "north-northeast", "northeast", "east-northeast",
        "east", "east-southeast", "southeast", "south-southeast",
        "south", "south-southwest", "southwest", "west-southwest",
        "west", "west-northwest", "northwest", "north-northwest"
    ]
    idx = round(deg / (360. / len(directions)))
    return directions[idx % len(directions)]


def beaufort_label(wind_speed: float) -> str:
    """
    Transforms wind speed to descriptive label using Beaufort scale.
    https://www.weather.gov/mfl/beaufort
    https://simple.wikipedia.org/wiki/Beaufort_scale
    """
    # scala speeds in m/s
    speeds = [
        0, 0.3, 1.5, 3.3, 5.5, 8.0, 10.8, 13.9,
        17.2, 20.7, 24.5, 28.4, 32.6, float('inf')
    ]

    # Description lables
    labels = [
        'Calm', 'Light air', 'Light breeze', 'Gentle breeze',
        'Moderate breeze', 'Fresh breeze', 'Strong breeze',
        'Near Gale', 'Fresh Gale', 'Strong Gale', 'Storm',
        'Violent storm', 'Hurricane-force'

    ]

    def lq(x: float) -> bool:
        """Less or equal"""
        return not x <= wind_speed

    lable_idx = speeds.index(
        list(filter(lq, speeds))[0]
    )-1

    return labels[lable_idx]


def get_wind(wind: dict) -> str:
    """
    Extract and transform wind data.
    """
    wind_speed = wind.get('speed', 0)
    return ', '.join([
        beaufort_label(wind_speed=wind_speed),
        '{0} m/s'.format(wind_speed),
        degrees_to_cardinal(deg=wind.get('deg', 0))
    ])


def get_hour(utc_time: int, timezone: int) -> str:
    """
    Extract and transform hour from UTC time and timezone.
    """
    return strftime("%H:%M", gmtime(utc_time + timezone))


def get_date(utc_time: int, timezone: int) -> str:
    """
    Extract and transform hour from UTC time and timezone.
    """
    return strftime("%Y-%m-%d %H:%M:%S", gmtime(utc_time + timezone))


def weather_request(city: str, country: str) -> dict:
    url = (
        OPENWEATHER_URL
        + '/data/2.5/weather?q={0},{1}&units=metric'.format(
            city, country
        )
        + '&appid={0}'.format(OPENWEATHER_APPID)
    )
    print('url: ', url)
    r = requests.get(url)
    return json.loads(r.text)


def forecast_request(lat: float, lon: float) -> dict:
    url = (
        OPENWEATHER_URL
        + '/data/2.5/onecall?lat={0}&lon={1}'.format(
            lat, lon
        )
        + '&exclude=current,hourly,minutely,alerts'
        + '&units=metric'
        + '&appid={0}'.format(OPENWEATHER_APPID)
    )
    print('url: ', url)
    r = requests.get(url)
    return json.loads(r.text)
