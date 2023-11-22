from datetime import datetime, date
from typing import List

from src.weather.services.interfaces import (
    IWeatherService,
    CityDoesNotExists,
    FailedToRetreiveData,
)
from src.weather.domain.models import Weather
from src.weather.adapters.repo import (
    CityRepo,
    WeatherRepo,
)
from src.sdk.openwr import OpenWeatherSDK


class WeatherService(IWeatherService):
    def __init__(
            self,
            weather_repo: WeatherRepo,
            city_repo: CityRepo,
            sdk: OpenWeatherSDK,
            default_city_name: str = 'Kyiv',
    ):
        self._wrepo: WeatherRepo = weather_repo
        self._crepo: CityRepo = city_repo
        self._sdk: OpenWeatherSDK = sdk
        self._default_city_name: str = default_city_name


    def fetch_curr_weather(self, city_name: str = None) -> Weather:
        '''
        Fetches and stores current weather for default city 
        if city_name isn't provided.
        '''
        name = city_name or self._default_city_name
        city = self._crepo.get_by_name(name)
        if not city:
            msg = f'Does not have city with name "{name}"'
            raise CityDoesNotExists(msg)


        # NOTE: doesn't check data that came from sdk 
        # only for simplicity purposes.
        # normally here should be used a serializer
        data = self._sdk.get_current_weather_by_city_id(city.city_id)

        if 'error' in data:
            raise FailedToRetreiveData(data['error'])

        return self.store_weather_data(
            weather=Weather(
                datetime=datetime.utcnow(),
                temp=data['main']['temp'],
                city=city,
                extra=data,
            ),
        )


    def store_weather_data(self, weather: Weather) -> Weather:
        '''Persists weather object.'''
        return self._wrepo.create(weather)


    def get_weather_by_city_name_date(self, dt: date, city_name: str = None) -> List[Weather]:
        '''Return weather objects filtered by city and date.'''
        city = self._crepo.get_by_name(city_name or self._default_city_name)
        if not city:
            raise CityDoesNotExists
        return self._wrepo.get_by_date(city.id, dt)
