import logging

from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import (
    registry,
    relationship,
)

from weather.domain.models import (
    City,
    Coord,
    Weather,
)


logger = logging.getLogger(__name__)


mapper_registry = registry()
metadata = mapper_registry.metadata


coords_table = Table(
    'coords_table',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True),
    Column('lon', Integer, nullable=False),
    Column('lat', Integer, nullable=False),
)


cities_table = Table(
    'cities_table',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True),
    Column('name', String(length=128), index=True),
    Column('city_id', Integer, nullable=False, index=True),
)


weathers_table = Table(
    'weathers_table',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True),
    Column('city_id', ForeignKey('cities_table.id', ondelete='CASCADE'), nullable=True),
    Column('coord_id', ForeignKey('coords_table.id', ondelete='CASCADE'), nullable=True),
    Column('temp', Integer, nullable=False),
    Column('extra', JSON, nullable=False, server_default='{}'),
    Column('datetime', DateTime, nullable=False),
)


def start_mappers():
    logger.info("Starting mappers")
    cities_mapper = mapper_registry.map_imperatively(City, cities_table)
    coords_mapper = mapper_registry.map_imperatively(Coord, coords_table)
    weathers_mapper = mapper_registry.map_imperatively(
        Weather,
        weathers_table,
        properties={
            'city': relationship(cities_mapper),
            'coord': relationship(coords_mapper),
        },
    )
