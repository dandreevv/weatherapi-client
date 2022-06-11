from abc import ABC, abstractmethod
from http import HTTPStatus

import attrs
import httpx

from .enteties import RealtimeWeather
from .helpers import raise_response_error


class ClientInterface(ABC):

    @abstractmethod
    def get_realtime_weather(self, location: str) -> RealtimeWeather:
        pass

    @abstractmethod
    def get_forecast_weather(self, location: str, days: int) -> dict:
        pass


@attrs.define(frozen=True)
class Client(ClientInterface):
    session: httpx.Client
    api_key: str

    def get_realtime_weather(self, location: str) -> dict:
        params = {
            "key": self.api_key,
            "q": location,
        }
        payload = self._request("/current.json", params=params)
        return payload

    def get_forecast_weather(self, location: str, days: int) -> dict:
        params = {
            "key": self.api_key,
            "q": location,
            "days": days,
        }
        payload = self._request("/forecast.json", params=params)
        return payload

    def _request(self, path: str, params: dict) -> dict:
        response = self.session.get(path, params=params)
        if response.status_code == HTTPStatus.OK:
            return response.json()

        raise_response_error(response)
