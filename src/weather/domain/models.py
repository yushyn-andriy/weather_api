from typing import Any, List
from datetime import datetime


def __repr__(attrs: List[str]):
    '''Simple function to prevent code duplication within __repr__ method.'''
    def f(self: Any) -> str:
        cls_name = self.__class__.__name__
        kv = [
            f'{k}={repr(getattr(self, k, None))}'
            for k in attrs
        ]
        s = ', '.join(kv)
        f_str = f'{cls_name}({s})'
        return f_str
    return f


def to_dict(attrs: List[str]):
    def f(self: Any) -> dict:
        return {
            k: getattr(self, k, None)
            for k in attrs
        }
    return f



class City:
    __repr__ = __repr__([
        'name', 'country', 'city_id',
        'lat', 'lon',
    ])
    to_dict = to_dict([
        'id', 'name', 'country',
        'city_id', 'lat', 'lon',
    ])

    def __init__(
            self,
            name: str,
            country: str,
            city_id: int,
            lat: float,
            lon: float,
    ) -> None:
        self.name: str = name
        self.country: str = country
        self.city_id: int =  city_id
        self.lat: float = lat
        self.lon: float = lon



class Weather:
    '''
    Represents the weather data at specific time 
    and at a specific location(city).
    '''

    __repr__ = __repr__(['datetime', 'temp', 'city'])
    to_dict = to_dict(['id', 'temp', 'datetime'])


    def __init__(
            self,
            datetime: datetime,
            temp: int,
            city: City,
            extra: str
    ) -> None:
        self.datetime: datetime = datetime
        self.temp: int = temp
        self.city: City = city
        self.extra: str =  extra
