import os
from pathlib import Path
import logging.config

from flask import Flask

from src.sdk.openwr import OpenWeatherSDK
from src.weather.adapters.repo import (
    CityRepo,
    WeatherRepo,
)
from src.weather.services.services import WeatherService
from . import db


def setup_logging(instance_path):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S',
        handlers=[
            logging.FileHandler(instance_path / 'log.txt'),
            logging.StreamHandler(),
        ]
    )


def init_applications(app):
    from . import db
    from . import manage
    from . import jobs

    db.init_app(app)
    manage.init_app(app)
    jobs.init_app(app)


def init_services(app):
    with app.app_context():
        session = db.get_db_session()
        weather_svc = WeatherService(
            WeatherRepo(session),
            CityRepo(session),
            OpenWeatherSDK(app.config['OPEN_WEATHER_API_KEY']),
            app.config['CITY_NAME'],
        )
        app.weather_svc = weather_svc


def register_blueprints(app):
    from .views import wbp
    app.register_blueprint(wbp)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    root_path = Path(app.root_path)
    instance_path = Path(app.instance_path)
    try:
        os.makedirs(instance_path)
    except FileExistsError:
        pass


    default_config_path = root_path.parent / 'config.py'
    app.config.from_pyfile(
        os.getenv('WEATHER_CONFIG_FILE', default_config_path),
        silent=False,
    )

    setup_logging(instance_path)

    # initializing applications, services, blueprints
    init_applications(app)
    init_services(app)
    register_blueprints(app)

    return app
