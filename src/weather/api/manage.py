import logging

import json
import click

from src.weather.adapters.repo import CityRepo
from src.weather.domain.models import City

from . import db


logger = logging.getLogger(__name__)


@click.command('dummy')
def dummy():
    '''Run dummy command.'''
    click.echo('Dummy has been executed.')


@click.command('load-city-list')
@click.argument('file', type=click.File('r', encoding='utf-8'))
def load_city_list(file):
    '''Load city-list from file.'''
    repo = CityRepo(db.get_db_session())
    
    try:
        text = file.read()
        data = json.loads(text)

        # NOTE: a serializer should be used 
        # TODO: add serializers for these purposes

        city_list = [
            City(
                name=item['name'],
                country=item['country'],
                city_id=item['id'],
                lat=item['coord']['lat'],
                lon=item['coord']['lon'],
            )
            for item in data
        ]
        
        # first delete all records within database 
        repo.clear_all()
        res = repo.bulk_create(city_list)

        click.echo(f'{len(res)} records has been created.')
    except json.JSONDecodeError as e:
        logger.error(f'error when parsing json "{e}"')
        click.echo('error when parsing json')
    finally:
        file.close()



def init_app(app):
    app.cli.add_command(dummy)
    app.cli.add_command(load_city_list)
