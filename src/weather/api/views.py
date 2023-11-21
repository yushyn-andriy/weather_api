from flask import (
    Blueprint
)

from weather.domain.models import *

wbp = Blueprint('weather', __name__, url_prefix='/api/v1')


@wbp.route('/_status', methods=['GET'])
def _ok():
    print(City('Kiev', 200))
    print(Coord(123, 200))
    return {
        'status': 'ok',
    }, 200
