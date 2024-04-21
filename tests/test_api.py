import json
from datetime import date
from pathlib import Path

from football_api.api import get_competitions, get_games


def test_get_games():
    result = get_games(date(2024, 4, 9), ['UEFA Liga dos Campeões'])
    expected = {
        'UEFA Liga dos Campeões': [
            {
                'home': {
                    'name': 'Arsenal',
                    'score': 2,
                    'image': 'https://images.onefootball.com/icons/teams/164/2.png',
                },
                'away': {
                    'name': 'Bayern de Munique',
                    'score': 2,
                    'image': 'https://images.onefootball.com/icons/teams/164/6.png',
                },
            },
            {
                'home': {
                    'name': 'Real Madrid',
                    'score': 3,
                    'image': 'https://images.onefootball.com/icons/teams/164/26.png',
                },
                'away': {
                    'name': 'Manchester City',
                    'score': 3,
                    'image': 'https://images.onefootball.com/icons/teams/164/209.png',
                },
            },
        ]
    }
    assert result == expected


def test_get_games_with_multiple_competitions():
    result = get_games(date(2024, 4, 20), ['Brasileirão', 'Premier League'])
    expected = {
        'Brasileirão': [
            {
                'home': {
                    'name': 'Fluminense',
                    'score': 2,
                    'image': 'https://images.onefootball.com/icons/teams/164/1666.png',
                },
                'away': {
                    'name': 'Vasco da Gama',
                    'score': 1,
                    'image': 'https://images.onefootball.com/icons/teams/164/1790.png',
                },
            },
            {
                'home': {
                    'name': 'Grêmio',
                    'score': 1,
                    'image': 'https://images.onefootball.com/icons/teams/164/1670.png',
                },
                'away': {
                    'name': 'Cuiabá',
                    'score': 0,
                    'image': 'https://images.onefootball.com/icons/teams/164/2704.png',
                },
            },
            {
                'home': {
                    'name': 'RB Bragantino',
                    'score': 1,
                    'image': 'https://images.onefootball.com/icons/teams/164/4734.png',
                },
                'away': {
                    'name': 'Corinthians',
                    'score': 0,
                    'image': 'https://images.onefootball.com/icons/teams/164/1649.png',
                },
            },
            {
                'home': {
                    'name': 'Atlético-MG',
                    'score': 3,
                    'image': 'https://images.onefootball.com/icons/teams/164/1683.png',
                },
                'away': {
                    'name': 'Cruzeiro',
                    'score': 0,
                    'image': 'https://images.onefootball.com/icons/teams/164/1794.png',
                },
            },
        ],
        'Premier League': [
            {
                'home': {
                    'name': 'Luton Town FC',
                    'score': 1,
                    'image': 'https://images.onefootball.com/icons/teams/164/599.png',
                },
                'away': {
                    'name': 'Brentford FC',
                    'score': 5,
                    'image': 'https://images.onefootball.com/icons/teams/164/671.png',
                },
            },
            {
                'home': {
                    'name': 'Sheffield United FC',
                    'score': 1,
                    'image': 'https://images.onefootball.com/icons/teams/164/583.png',
                },
                'away': {
                    'name': 'Burnley',
                    'score': 4,
                    'image': 'https://images.onefootball.com/icons/teams/164/275.png',
                },
            },
            {
                'home': {
                    'name': 'Wolverhampton Wanderers',
                    'score': 0,
                    'image': 'https://images.onefootball.com/icons/teams/164/203.png',
                },
                'away': {
                    'name': 'Arsenal',
                    'score': 2,
                    'image': 'https://images.onefootball.com/icons/teams/164/2.png',
                },
            },
        ],
    }
    assert result == expected


def test_get_games_with_all_competitions():
    result = get_games(date(2024, 4, 9))
    json.dump(
        result, open(Path('tests') / 'games-with-all-competitions.json', 'w')
    )
    expected = json.load(
        open(Path('tests') / 'games-with-all-competitions.json', 'r')
    )
    assert result == expected


def test_get_competitions():
    result = get_competitions(date(2024, 4, 17))
    expected = [
        'Brasileirão',
        'UEFA Liga dos Campeões',
        'Taça de Portugal',
        '1. SNL',
        '1ª HNL',
        '2. Lig',
        'AFC Champions League',
        'AFC Cup',
        'AFC U-23 Asian Cup',
        'Acreano',
        'Bulgarian Cup',
        'CBF Brasileiro U20',
        'Campeonato Armênio',
        'Campeonato Nacional Feminino',
        'Copa Argentina',
        'Copa Verde',
        'Copa da Coreia',
        'Copa de la Liga Profesional',
        'Copa do Brasil U17',
        'Cupa Romaniei',
        'Cypriot Cup',
        'Czech Fortuna národní liga',
        'Egyptian Premier League',
        'Eliteserien',
        'Honduras Liga Nacional',
        'Hong Kong Premier League',
        'J.League Cup',
        'Kubok',
        'Liga 1',
        'Liga Nacional de Guatemala',
        'Liga Principal de Futebol',
        'Liga Pro',
        'Liga das Estrelas',
        'Liga de Expansión MX',
        'Liga de Fútbol de Primera División',
        'Liga do Golfo Arábico',
        'LigaPro Serie A',
        'Meistriliiga',
        'National League',
        'Primera A Apertura',
        'Primera División',
        'Primera División Apertura',
        'Primera Nacional',
        'Regionalliga Nord',
        'Regionalliga Südwest',
        'Rondoniense',
        'SWPL 1',
        'Scottish Premiership',
        'Slovak Cup',
        'Suomen Cup',
        'Super Liga Feminina FA',
        'Taça do Open dos Estados Unidos',
        'Tonybet Virsliga',
        'Torneo Apertura',
        'VBet Premyer Liga',
    ]
    assert result == expected
