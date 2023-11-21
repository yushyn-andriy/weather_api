from typing import Any, List
from datetime import datetime

def __repr__(attrs: List[str]):
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


class Coord:
    __repr__ = __repr__(['lon', 'lat'])

    def __init__(self, lon: int, lat: int) -> None:
        self.lon = lon
        self.lat = lat


class City:
    __repr__ = __repr__(['name', 'city_id'])

    def __init__(self, name: str, city_id: int) -> None:
        self.name: str = name
        self.city_id: int =  city_id


class Weather:
    '''
    Represents the weather data at specific time 
    and at a specific location(city).
    '''

    __repr__ = __repr__(['datetime', 'temp', 'location'])


    def __init__(
            self,
            datetime: datetime,
            temp: int,
            coord: Coord,
            city: City,
            extra: str
    ) -> None:
        self.datetime: datetime = datetime
        self.temp: int = temp
        self.coord: Coord = coord
        self.city: City = city
        self.extra: str =  extra
