import logging

from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Float,
)
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import (
    registry,
    relationship,
)

from src.weather.domain.models import (
    City,
    Weather,
)


logger = logging.getLogger(__name__)


mapper_registry = registry()
metadata = mapper_registry.metadata


cities_table = Table(
    'cities_table',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True),
    Column('name', String(length=128), index=True),
    Column('country', String(length=128), server_default='', index=False),
    Column('city_id', Integer, nullable=False, index=True),
    Column('lat', Float, nullable=False),
    Column('lon', Float, nullable=False),
)


weathers_table = Table(
    'weathers_table',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True),
    Column('city_id', ForeignKey('cities_table.id', ondelete='CASCADE'), nullable=True),
    Column('temp', Float, nullable=False),
    Column('extra', JSON, nullable=False, server_default='{}'),
    Column('datetime', DateTime, nullable=False),
)


def start_mappers():
    '''
    Map objects to sql tables.
    Such approach decreases a code coupling.
    '''
    logger.info("Starting mappers")
    cities_mapper = mapper_registry.map_imperatively(City, cities_table)
    mapper_registry.map_imperatively(
        Weather,
        weathers_table,
        properties={
            'city': relationship(cities_mapper),
        },
    )
