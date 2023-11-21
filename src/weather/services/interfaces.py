from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import List

from src.weather.domain.models import Weather


class IWeatherService:
    def fetch_curr_weather_by_city_id(self, city_id: str) -> Weather:
        raise NotImplementedError

    def store_weather_data(self, weather: Weather) -> None:
        raise NotImplementedError

    def get_weather_by_date(self, dt: date) -> List[Weather]:
        raise NotImplementedError
