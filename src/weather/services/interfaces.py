from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import List

from src.weather.domain.models import Weather


class CityDoesNotExists(Exception):
    '''Raises when city was not found.'''


class FailedToRetreiveData(Exception):
    '''Raises failed to retrieve data.'''


class IWeatherService:
    '''Main interface that describes API to interact with weather service.'''

    def fetch_curr_weather(self, city_name: str = None) -> Weather:
        raise NotImplementedError

    def store_weather_data(self, weather: Weather) -> None:
        raise NotImplementedError

    def get_weather_by_date(self, dt: date) -> List[Weather]:
        raise NotImplementedError
