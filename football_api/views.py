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

    @app.get('/jogos/<date_string>/<competition>')
    def games_by_competition(date_string, competition):
        if date_string == 'live':
            return jsonify(get_games(date.today(), live=True))
        else:
            return jsonify(
                get_games(get_date(date_string), [competition])
            )

    @app.get('/jogos/<date_string>')
    def games(date_string):
        if date_string == 'live':
            return jsonify(get_games(date.today(), live=True))
        else:
            return jsonify(get_games(get_date(date_string)))

    @app.get('/competicoes/<date_string>')
    def competitions(date_string):
        return jsonify(get_competitions(get_date(date_string)))
