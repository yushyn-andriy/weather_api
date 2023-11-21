import os
from pathlib import Path
import logging.config

from flask import Flask


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


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # current dir
    root_path = Path(app.root_path)
    instance_path = Path(app.instance_path)

    default_config_path = root_path.parent / 'config.py'
    app.config.from_pyfile(
        os.getenv('WEATHER_CONFIG_FILE', default_config_path),
        silent=False,
    )

    setup_logging(instance_path)

    try:
        os.makedirs(instance_path)
    except OSError:
        pass


    # register all applications
    from . import db
    db.init_app(app)

    # register all blueprints
    from .views import wbp
    app.register_blueprint(wbp)

    return app
