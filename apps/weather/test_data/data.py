"""
Testing Data
"""


openweather_data = {
    "coord": {
        "lon": -74.0817,
        "lat": 4.6097
    },
    "weather": [
        {
            "id": 801,
            "main": "Clouds",
            "description": "few clouds",
            "icon": "02n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 7,
        "feels_like": 4.86,
        "temp_min": 7,
        "temp_max": 7,
        "pressure": 1026,
        "humidity": 100
    },
    "visibility": 10000,
    "wind": {
        "speed": 2.06,
        "deg": 330
    },
    "clouds": {
        "all": 20
    },
    "dt": 1610606854,
    "sys": {
        "type": 1,
        "id": 8582,
        "country": "CO",
        "sunrise": 1610622533,
        "sunset": 1610665300
    },
    "timezone": -18000,
    "id": 3688689,
    "name": "Bogotá",
    "cod": 200
}


weather = {
    "location_name": "Bogotá, CO",
    "temperature": "7 °C",
    "wind": "Light breeze, 2.06 m/s, north-northwest",
    "cloudiness": "Few clouds",
    "pressure": "1026 hpa",
    "humidity": "100%",
    "sunrise": "06:08",
    "sunset": "18:01",
    "geo_coordinates": "[4.61, -74.08]",
    "requested_time": "2021-01-14 01:47:34",
    "forecast": None
}


openweather_forecast_data =  {
    "dt": 1610643600,
    "sunrise": 1610622886,
    "sunset": 1610664548,
    "temp": {
        "day": 305.33,
        "min": 294.87,
        "max": 306.7,
        "night": 296.8,
        "eve": 300.19,
        "morn": 294.87
    },
    "feels_like": {
        "day": 305.54,
        "night": 298.62,
        "eve": 301.22,
        "morn": 294.89
    },
    "pressure": 1010,
    "humidity": 41,
    "dew_point": 290.6,
    "wind_speed": 3.24,
    "wind_deg": 46,
    "weather": [
        {
            "id": 802,
            "main": "Clouds",
            "description": "scattered clouds",
            "icon": "03d"
        }
    ],
    "clouds": 42,
    "pop": 0.07,
    "uvi": 11.41
}


forecast = {
    "forecast_date": "2021-01-14 12:00:00",
    "temperature": "305.33 °C",
    "wind": "Light breeze, 3.24 m/s, northeast",
    "cloudiness": "Scattered clouds",
    "pressure": "1010 hpa",
    "humidity": "41%",
    "sunrise": "06:14",
    "sunset": "17:49"
}


deg_directions = {
    0: 'north',
    22: 'north-northeast',
    44: 'northeast',
    66: 'east-northeast',
    88: 'east',
    110: 'east-southeast',
    132: 'southeast',
    154: 'south-southeast',
    176: 'south',
    198: 'south-southwest',
    220: 'southwest',
    242: 'west-southwest',
    264: 'west',
    286: 'west-northwest',
    308: 'northwest',
    330: 'north-northwest'
}


beaufort_labels = {
    0.2: 'Calm',
    1.4: 'Light air',
    3.2: 'Light breeze',
    5.4: 'Gentle breeze',
    7.9: 'Moderate breeze',
    10.7: 'Fresh breeze',
    13.8: 'Strong breeze',
    17.1: 'Near Gale',
    20.6: 'Fresh Gale',
    24.4: 'Strong Gale',
    28.3: 'Storm',
    32.5: 'Violent storm',
    35: 'Hurricane-force'
}