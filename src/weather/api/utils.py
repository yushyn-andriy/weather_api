import re
from datetime import datetime, date


def is_valid_date(s: str) -> bool:
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, s))


def convert_to_date(s: str) -> date:
    '''Converts string to python date object.'''
    try:
        return datetime.strptime(s, '%Y-%m-%d').date()
    except ValueError:
        return None