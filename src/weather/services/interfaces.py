from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import List

from src.weather.domain.models import Temp


class IWeatherService:
    def fetch_temp(self, dt: datetime, location: str) -> Temp:
        raise NotImplementedError
    
    def store_temp(self, temp: Temp) -> None:
        raise NotImplementedError
    
    def get_temp_by_date(self, dt: date) -> List[Temp]:
        raise NotImplementedError
