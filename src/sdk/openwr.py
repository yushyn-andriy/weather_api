import requests
from requests.exceptions import RequestException

URL = 'https://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units={}'
DEFAULT_UNITS = 'metric'


class OpenWeatherSDK:

    def __init__(self, api_key: str, units: str = DEFAULT_UNITS):
        self._api_key = api_key
        self._default_units = units
    

    def get_current_weather_by_city_id(self, city_id: int) -> dict:
        try:
            response = requests.get(
                URL.format(city_id, self._api_key, self._default_units))
            response.raise_for_status()  # Raises HTTPError for bad requests (4XX or 5XX)
            return response.json()
        except RequestException as e:
            return {"error": f"Failed to retrieve data: {e}"}
        except ValueError as e:
            return {"error": f"Invalid response received: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}
