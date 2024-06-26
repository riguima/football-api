import json
from pathlib import Path

from flask import url_for


def test_games_by_competition(client):
    result = client.get(
        url_for(
            'games_by_competition',
            date_string='2024-04-18',
            competition='UEFA Liga Europa',
        )
    ).json
    expected = {
        'UEFA Liga Europa': [
            {
                'away': {
                    'image': 'https://images.onefootball.com/icons/teams/164/18.png',
                    'name': 'Liverpool',
                    'score': 1,
                },
                'home': {
                    'image': 'https://images.onefootball.com/icons/teams/164/248.png',
                    'name': 'Atalanta',
                    'score': 0,
                },
            },
            {
                'away': {
                    'image': 'https://images.onefootball.com/icons/teams/164/162.png',
                    'name': 'Bayer Leverkusen',
                    'score': 1,
                },
                'home': {
                    'image': 'https://images.onefootball.com/icons/teams/164/198.png',
                    'name': 'West Ham',
                    'score': 1,
                },
            },
            {
                'away': {
                    'image': 'https://images.onefootball.com/icons/teams/164/23.png',
                    'name': 'Milan',
                    'score': 1,
                },
                'home': {
                    'image': 'https://images.onefootball.com/icons/teams/164/145.png',
                    'name': 'Roma',
                    'score': 2,
                },
            },
            {
                'away': {
                    'image': 'https://images.onefootball.com/icons/teams/164/147.png',
                    'name': 'Benfica',
                    'score': 0,
                },
                'home': {
                    'image': 'https://images.onefootball.com/icons/teams/164/22.png',
                    'name': 'Marselha',
                    'score': 1,
                },
            },
        ]
    }
    assert result == expected


def test_live_games_by_competition(client):
    result = client.get(url_for('games', date_string='live', competition='LaLiga'))
    assert result.status_code == 200


def test_today_games_by_competition(client):
    result = client.get(url_for('games', date_string='hoje', competition='UEFA Liga Europa'))
    assert result.status_code == 200


def test_yesterday_games_by_competition(client):
    result = client.get(url_for('games', date_string='ontem', competition='UEFA Liga Europa'))
    assert result.status_code == 200


def test_tomorrow_games_by_competition(client):
    result = client.get(url_for('games', date_string='amanha', competition='UEFA Liga Europa'))
    assert result.status_code == 200


def test_games(client):
    result = client.get(url_for('games', date_string='2024-04-09')).json
    expected = json.load(
        open(Path('tests') / 'games-with-all-competitions.json')
    )
    assert result == expected


def test_live_games(client):
    result = client.get(url_for('games', date_string='live'))
    assert result.status_code == 200


def test_today_games(client):
    result = client.get(url_for('games', date_string='hoje'))
    assert result.status_code == 200


def test_yesterday_games(client):
    result = client.get(url_for('games', date_string='ontem'))
    assert result.status_code == 200


def test_tomorrow_games(client):
    result = client.get(url_for('games', date_string='amanha'))
    assert result.status_code == 200


def test_competitions(client):
    result = client.get(url_for('competitions', date_string='2024-04-15')).json
    expected = [
        'LaLiga',
        'Premier League',
        'Serie A',
        'Liga Portugal',
        'Brasileirão Feminino',
        '1 Liga Bank Asya',
        '1. SNL',
        'AFC U-23 Asian Cup',
        'Acreano',
        'Allsvenskan',
        'Amapaense',
        'Botola',
        'Campeonato Islandês',
        'Cearense 2',
        'Championnat National',
        'Copa de la Liga Profesional',
        'Divisão Principal',
        'Eerste Divisie',
        'Egyptian Premier League',
        'Ekstraklasa',
        'Football National League 2',
        'Frauen-Bundesliga',
        'Iraq Stars League',
        'Liga 1',
        'Liga MX Femenil',
        'Liga Nacional de Futebol',
        'Liga Premier',
        'Liga Principal de Futebol',
        'Liga Profissional Búlgara',
        'Liga do Golfo Arábico',
        'LigaPro Serie A',
        'Ligat HaAl',
        'Ligue 2',
        'MLS Next Pro',
        'National League',
        'Peru Liga 1',
        'Primeiro B',
        'Primera B',
        'Primera División',
        'Regionalliga West',
        'Segunda Divisão',
        'Serie A Women',
        'Serie C',
        'Suomen Cup',
        'Super Liga da India',
        'SuperLiga',
        'Superettan',
        'Superleague 2',
        'Superliga',
        'Superligaen',
        'Süper Lig',
        'Torneo Apertura',
        'VBet Premyer Liga',
    ]
    assert result == expected


def test_today_competitions(client):
    result = client.get(url_for('competitions', date_string='hoje'))
    assert result.status_code == 200


def test_yesterday_competitions(client):
    result = client.get(url_for('competitions', date_string='ontem'))
    assert result.status_code == 200


def test_tomorrow_competitions(client):
    result = client.get(url_for('competitions', date_string='amanha'))
    assert result.status_code == 200
