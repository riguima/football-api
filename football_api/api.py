import json
import re

from httpx import get
from rich import print


def get_games(games_date, competitions):
    result = {}
    response = get(
        f'https://onefootball.com/pt-br/jogos?date={games_date:%Y-%m-%d}'
    )
    data = json.loads(
        re.findall(r'\{"props".+\}', response.text, re.DOTALL)[0]
    )
    for container in data['props']['pageProps']['containers']:
        matchs = container['type']['fullWidth']['component'][
            'contentType'
        ].get('matchCardsList')
        if matchs:
            for match in matchs['matchCards']:
                competition = match['trackingEvents'][0][
                    'typedServerParameter'
                ]['competition']['value']
                if competition in competitions:
                    game = {
                        'home': {
                            'name': match['homeTeam']['name'],
                            'score': int(
                                match['homeTeam']['score'].split(' ')[0]
                            ),
                            'image': match['homeTeam']['imageObject']['path'],
                        },
                        'away': {
                            'name': match['awayTeam']['name'],
                            'score': int(
                                match['awayTeam']['score'].split(' ')[0]
                            ),
                            'image': match['awayTeam']['imageObject']['path'],
                        },
                    }
                    if result.get(competition):
                        result[competition].append(game)
                    else:
                        result[competition] = [game]
    return result
