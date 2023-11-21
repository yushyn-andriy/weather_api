from abc import abstractmethod
from datetime import datetime, date
from typing import List

from src.weather.services.interfaces import IWeatherService
from src.weather.domain.models import Weather


class WeatherService(IWeatherService):
    def __init__(self, repo, sdk):
        self._repo = repo
        self._sdk = sdk

    def fetch_curr_weather_by_city_id(self, city_id: str) -> Weather:
        raise NotImplementedError

    def store_weather_data(self, weather: Weather) -> None:
        raise NotImplementedError

    def get_weather_by_date(self, dt: date) -> List[Weather]:
        raise NotImplementedError
