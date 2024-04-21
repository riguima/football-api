from datetime import datetime

from flask import jsonify

from football_api.api import get_games


def init_app(app):
    @app.get('/games/<date>/<competition>')
    def games(date, competition):
        return jsonify(
            get_games(datetime.strptime(date, '%Y-%m-%d'), [competition])
        )
