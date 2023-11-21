import os

SECRET_KEY = os.getenv('WEATHER_SECRET_KEY', 'dev1') 
DATABASE = os.getenv('WEATHER_DATABASE', 'sqlite:///instance/db.sqlite') 
CITY_TO_FETCH_WEATHER = os.getenv('WEATHER_CITY_TO_FETCH', 'Kyiv')
