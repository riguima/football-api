from datetime import datetime, date, timedelta

from flask import jsonify

from football_api.api import get_competitions, get_games


def init_app(app):
    def get_date(date_string):
        if date_string == 'hoje':
            return date.today()
        elif date_string == 'amanha':
            return date.today() + timedelta(days=1)
        elif date_string == 'ontem':
            return date.today() - timedelta(days=1)
        else:
            return datetime.strptime(date_string, '%Y-%m-%d')

    @app.get('/jogos/<date>/<competition>')
    def games_by_competition(date, competition):
        return jsonify(
            get_games(get_date(date), [competition])
        )

    @app.get('/jogos/<date>')
    def games(date):
        return jsonify(get_games(get_date(date)))

    @app.get('/competicoes/<date>')
    def competitions(date):
        return jsonify(get_competitions(get_date(date)))
