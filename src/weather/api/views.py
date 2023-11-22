from flask import (
    Blueprint,
    request,
    current_app,
)

from . import utils
from . import auth

wbp = Blueprint('weather', __name__, url_prefix='/api/v1')


@wbp.route('/_status', methods=['GET'])
def _ok():
    return {
        'status': 'ok',
    }, 200


@wbp.route('/weather', methods=['GET'])
def weather():    
    weather_svc = current_app.weather_svc

    token = request.headers.get('x-token', None)
    if not token or not auth.check_x_token(token):
        return {
            'status': 'Unauthorized',
            'message': 'valid 32 character length "x-token" must be provided via header.',
        }, 401

    day = request.args.get('day', None)
    if not day:
        return {
            'status': 'Bad request',
            'message': 'Get parameter "day" must be provided',
        }, 400
    if not utils.is_valid_date(day):
        return {
            'status': 'Bad request',
            'message': 'Wrong "day" format, should be "Y-m-d"',
        }, 400

    date = utils.convert_to_date(day)
    items = weather_svc.get_weather_by_city_name_date(date)

    return [
        item.to_dict()
        for item in items
    ], 200
