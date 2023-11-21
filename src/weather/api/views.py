from flask import (
    Blueprint
)


wbp = Blueprint('weather', __name__, url_prefix='/api/v1')


@wbp.route('/_status', methods=['GET'])
def _ok():
    return {
        'status': 'ok',
    }, 200
