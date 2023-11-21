import logging

import click
from flask import current_app, g

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


from weather.adapters.orm import metadata, start_mappers


logger = logging.getLogger(__name__)


def get_engine():
    logger.info('Get engine')
    return create_engine(current_app.config['DATABASE'])


def get_db_session():
    logger.info('Get session')
    if 'db' not in g:
        engine = get_engine()
        g.db = Session(engine)
    return g.db


def close_db(e=None):
    logger.info('Close session')
    db = g.pop('db', None)
    if db is not None:
        db.close()


@click.command('init-db')
def init_db_command():
    '''Initialize the database.'''
    metadata.create_all(get_engine())
    start_mappers()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
