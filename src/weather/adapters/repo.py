import logging
from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from src.weather.domain.models import (
    City,
    Weather,
)


logger = logging.getLogger(__name__)


class BaseRepo:
    def __init__(self, session: Session):
        self._session: Session = session

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()


class WeatherRepo(BaseRepo):
    MAX_ROWS_PER_DATE = 48

    def create(self, w: Weather) -> Weather:
        '''Persists a weather object.'''
        self._session.add(w)
        self.commit()
        return w

    def get_by_date(self, city_id: int, date: date) -> list[Weather]:
        '''
        Get weather by city_id and date.
        Here city_id represent the identifier within database NOT City CODE.
        '''
        return self._session.query(Weather).filter(
            Weather.city_id == city_id,
            func.date(Weather.datetime) == date,
        ).order_by(Weather.datetime).limit(self.MAX_ROWS_PER_DATE).all()


class CityRepo(BaseRepo):
    def create(self, c: City) -> City:
        '''Persists a city object.'''
        self._session.add(c)
        self.commit()
        return c

    def bulk_create(self, city_list: list[City]) -> list[int]:
        '''Bulk saves objects.'''
        try:
            self._session.bulk_save_objects(city_list, return_defaults=False)
            self.commit()
            return [item.id for item in city_list]
        except BaseException as e:
            logger.error(f'city list bulk create error: {e}')
            self.rollback()
            raise BaseException from e


    def get_by_name(self, city_name: str) -> City:
        '''Returns a city object by name.'''
        return self._session.query(City).filter(
            City.name == city_name,
        ).first()


    def clear_all(self) -> None:
        '''Deletes all the city objects from database.'''
        try:
            self._session.query(City).delete()
            self._session.commit()
        except BaseException as e:
            logger.error('error: {e}')
            self.rollback()
