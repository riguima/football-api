from flask import url_for


def test_games(client):
    result = client.get(
        url_for('games', date='2024-04-18', competition='UEFA Liga Europa')
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
