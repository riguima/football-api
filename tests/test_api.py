from datetime import date

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from sofascore_api.api import get_games


@pytest.fixture(scope='session')
def driver():
    return Chrome(service=Service(ChromeDriverManager().install()))


def test_get_games(driver):
    result = get_games(driver, date(2024, 4, 9), ['UEFA Champions League'])
    expected = {
        'UEFA Champions League': [
            {
                'home': {
                    'name': 'Arsenal',
                    'goals': 2,
                    'image': 'https://api.sofascore.app/api/v1/team/42/image',
                },
                'away': {
                    'name': 'FC Bayern München',
                    'goals': 2,
                    'image': 'https://api.sofascore.app/api/v1/team/2672/image',
                },
            },
            {
                'home': {
                    'name': 'Real Madrid',
                    'goals': 3,
                    'image': 'https://api.sofascore.app/api/v1/team/2829/image',
                },
                'away': {
                    'name': 'Manchester City',
                    'goals': 3,
                    'image': 'https://api.sofascore.app/api/v1/team/17/image',
                },
            },
        ]
    }
    assert result == expected


def test_get_games_with_multiple_competitions(driver):
    result = get_games(
        driver, date(2024, 4, 20), ['Brasileirão Série A', 'Premier League']
    )
    expected = {
        'Brasileirão Série A': [
            {
                'home': {
                    'name': 'Fluminense',
                    'goals': 2,
                    'image': 'https://api.sofascore.app/api/v1/team/1961/image',
                },
                'away': {
                    'name': 'Vasco da Gama',
                    'goals': 1,
                    'image': 'https://api.sofascore.app/api/v1/team/1974/image',
                },
            },
            {
                'home': {
                    'name': 'Grêmio',
                    'goals': 1,
                    'image': 'https://api.sofascore.app/api/v1/team/5926/image',
                },
                'away': {
                    'name': 'Cuiabá',
                    'goals': 0,
                    'image': 'https://api.sofascore.app/api/v1/team/49202/image',
                },
            },
            {
                'home': {
                    'name': 'Red Bull Bragantino',
                    'goals': 1,
                    'image': 'https://api.sofascore.app/api/v1/team/1999/image',
                },
                'away': {
                    'name': 'Corinthians',
                    'goals': 0,
                    'image': 'https://api.sofascore.app/api/v1/team/1957/image',
                },
            },
            {
                'home': {
                    'name': 'Atlético Mineiro',
                    'goals': 3,
                    'image': 'https://api.sofascore.app/api/v1/team/1977/image',
                },
                'away': {
                    'name': 'Cruzeiro',
                    'goals': 0,
                    'image': 'https://api.sofascore.app/api/v1/team/1954/image',
                },
            },
        ],
        'Premier League': [
            {
                'home': {
                    'name': 'Luton Town',
                    'goals': 1,
                    'image': 'https://api.sofascore.app/api/v1/team/72/image',
                },
                'away': {
                    'name': 'Brentford',
                    'goals': 5,
                    'image': 'https://api.sofascore.app/api/v1/team/50/image',
                },
            },
            {
                'home': {
                    'name': 'Sheffield United',
                    'goals': 1,
                    'image': 'https://api.sofascore.app/api/v1/team/15/image',
                },
                'away': {
                    'name': 'Burnley',
                    'goals': 4,
                    'image': 'https://api.sofascore.app/api/v1/team/6/image',
                },
            },
            {
                'home': {
                    'name': 'Wolverhampton',
                    'goals': 0,
                    'image': 'https://api.sofascore.app/api/v1/team/3/image',
                },
                'away': {
                    'name': 'Arsenal',
                    'goals': 2,
                    'image': 'https://api.sofascore.app/api/v1/team/42/image',
                },
            },
        ],
    }
    assert result == expected
