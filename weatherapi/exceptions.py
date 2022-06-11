__all__ = (
    "WeatherAPIException",
    "APIKeyInvalid",
    "APIKeyDisabled",
    "APIKeyLimit",
    "LocationNotFound",
    "InternalError",
)


class WeatherAPIException(Exception):
    pass


class APIKeyInvalid(WeatherAPIException):
    pass


class APIKeyDisabled(WeatherAPIException):
    pass


class APIKeyLimit(WeatherAPIException):
    pass


class LocationNotFound(WeatherAPIException):
    pass


class InternalError(WeatherAPIException):
    pass
