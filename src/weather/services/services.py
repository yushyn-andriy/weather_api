from abc import abstractmethod
from datetime import datetime, date
from typing import List

from src.weather.services.interfaces import IWeatherService
from src.weather.domain.models import Temp


class WeatherService(IWeatherService):
    def __init__(self, repo, sdk):
        self._repo = repo
        self._sdk = sdk

    def fetch_temp(self, dt: datetime, location: str) -> Temp:
        raise NotImplementedError

    def store_temp(self, temp: Temp) -> None:
        raise NotImplementedError
    
    def get_temp_by_date(self, dt: date) -> List[Temp]:
        raise NotImplementedError
