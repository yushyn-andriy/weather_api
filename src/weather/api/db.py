import logging

import click
from flask import current_app, g

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.weather.adapters.orm import metadata, start_mappers


logger = logging.getLogger(__name__)


start_mappers()


def get_engine():
    '''Creates an engine.'''
    logger.info('get engine')
    return create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])


def get_db_session():
    '''Creates a db session.'''
    logger.info('get session')
    if 'db' not in g:
        engine = get_engine()
        g.db = Session(engine)
    return g.db


def close_db(e=None):
    '''Closes a db session.'''
    logger.info('close db session')
    db = g.pop('db', None)
    if db is not None:
        try:
            logger.info('commit changes')
            db.commit()
        except BaseException as e:
            logger.error(f'error when commiting {e}')
            logger.info(f'rollback changes')
            db.rollback()
        finally:
            logger.info('finally close the session')
            db.close()


@click.command('init-db')
def init_db_command():
    '''Initialize the database.'''
    metadata.create_all(get_engine())


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
