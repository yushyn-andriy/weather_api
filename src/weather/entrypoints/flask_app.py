from flask import Flask



app = Flask(__name__)


@app.route('/_status', methods=['GET'])
def _ok():
    return {
        'status': 'ok',
    }, 200
