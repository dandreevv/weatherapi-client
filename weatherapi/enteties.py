from enum import unique, Enum

import attrs
from datetime import datetime


__all__ = (
    "ErrorCode",
    "Location",
    "ConditionDescription",
    "RealtimeWeatherDescription",
    "RealtimeWeather",
)


@unique
class ErrorCode(Enum):
    API_KEY_MISSED = 1002
    API_KEY_INVALID = 2006
    API_KEY_DISABLED = 2008
    REQUESTS_LIMIT = 2007
    Q_MISSED = 1003
    LOCATION_NOT_FOUND = 1006
    URL_INVALID = 1005
    INTERNAL_ERROR = 9999


@attrs.define(frozen=True)
class Location:
    name: str            # Local area name
    region: str          # Local area region
    country: str         # Country
    latitude: str        # Latitude
    longitude: str       # Longitude
    localtime: datetime  # Local date and time


@attrs.define(frozen=True)
class ConditionDescription:
    text: str  # Condition text
    icon: str  # Icon URL
    code: int  # Condition unique code


@attrs.define(frozen=True)
class RealtimeWeatherDescription:
    last_updated: datetime  # Local date and time when data was updated
    temp_c: float            # Temperature in Celsius
    temp_f: float            # Temperature in Fahrenheit
    is_day: bool            # Is it day or night
    condition: ConditionDescription  # Weather condition description
    wind_mph: float          # Wind speed in miles
    wind_kph: float          # Wind speed in kilometers
    wind_direction_degree: float  # Wind direction in degrees
    wind_direction: str     # Wind direction as 16 point compass. e.g.: NSW
    pressure_mb: float       # Pressure in millibars
    pressure_in: float       # Pressure in inches
    precip_mm: float         # Precipitation amount in millimeters
    precip_in: float         # Precipitation amount in inches
    humidity: int           # Humidity as percentage
    cloud: int              # Cloud cover as percentage
    feelslike_c: float       # Feels like temperature in Celsius
    feelslike_f: float       # Feels like temperature in Fahrenheit
    vis_km: float            # Visibility in kilometers
    vis_miles: float         # Visibility in miles
    uv: float                # UV Index
    gust_mph: float          # Wind gust in miles per hour
    gust_kph: float          # Wind gust in kilometer per hour


@attrs.define(frozen=True)
class RealtimeWeather:
    location: Location
    weather: RealtimeWeatherDescription

