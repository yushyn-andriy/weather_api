import logging
from functools import wraps

from apscheduler.schedulers.background import BackgroundScheduler


logger = logging.getLogger(__name__)

sched = BackgroundScheduler(daemon=True)


def job(f, app):
    @wraps(f)
    def wrapped():
        with app.app_context():
            f(app)
    return wrapped


def dummy_job(app):
    '''Function for test purposes.'''
    logger.info("dummy_job scheduler is alive!")


def fetch_curr_weather_job(app):
    '''Fetches and stores current weather for default city.'''
    with app.app_context():
        w = app.weather_svc.fetch_curr_weather()
        logger.info(f'fethched weather data {w}')


def init_app(app):
    sched.add_job(job(dummy_job, app), 'interval', seconds=60)
    sched.add_job(job(fetch_curr_weather_job, app), 'interval', seconds=60)
    sched.start()
