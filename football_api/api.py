import json
import re

from httpx import get


def get_data(date):
    response = get(f'https://onefootball.com/pt-br/jogos?date={date:%Y-%m-%d}')
    return json.loads(
        re.findall(r'\{"props".+\}', response.text, re.DOTALL)[0]
    )


def get_matches(data):
    result = []
    for container in data['props']['pageProps']['containers']:
        matches = container['type']['fullWidth']['component'][
            'contentType'
        ].get('matchCardsList')
        if matches:
            result.extend(matches['matchCards'])
    return result


def get_games(date, competitions=[]):
    result = {}
    data = get_data(date)
    for match in get_matches(data):
        competition = match['trackingEvents'][0]['typedServerParameter'][
            'competition'
        ]['value']
        if competition in competitions or not competitions:
            home_score = match['homeTeam']['score'].split(' ')[0]
            away_score = match['awayTeam']['score'].split(' ')[0]
            game = {
                'home': {
                    'name': match['homeTeam']['name'],
                    'score': 0 if not home_score else int(home_score),
                    'image': match['homeTeam']['imageObject']['path'],
                },
                'away': {
                    'name': match['awayTeam']['name'],
                    'score': 0 if not away_score else int(away_score),
                    'image': match['awayTeam']['imageObject']['path'],
                },
            }
            if result.get(competition):
                result[competition].append(game)
            else:
                result[competition] = [game]
    return result


def get_competitions(date):
    result = []
    data = get_data(date)
    for match in get_matches(data):
        competition = match['trackingEvents'][0]['typedServerParameter'][
            'competition'
        ]['value']
        if competition not in result:
            result.append(competition)
    return result
