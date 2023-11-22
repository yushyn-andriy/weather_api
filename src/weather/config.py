import os

SECRET_KEY = os.getenv('WEATHER_SECRET_KEY', 'dev') 
SQLALCHEMY_DATABASE_URI = os.getenv('WEATHER_SQLALCHEMY_DATABASE_URI', 'sqlite:///instance/db.sqlite') 
CITY_NAME = os.getenv('WEATHER_CITY_NAME', 'Kyiv')
OPEN_WEATHER_API_KEY = os.getenv('WEATHER_OPEN_API_KEY', None)

# should be provided
assert OPEN_WEATHER_API_KEY
