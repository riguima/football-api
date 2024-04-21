from datetime import datetime

from flask import jsonify

from football_api.api import get_competitions, get_games


def init_app(app):
    @app.get('/games/<date>/<competition>')
    def games(date, competition):
        return jsonify(
            get_games(datetime.strptime(date, '%Y-%m-%d'), [competition])
        )

    @app.get('/games/<date>')
    def competitions(date):
        return jsonify(get_competitions(datetime.strptime(date, '%Y-%m-%d')))
