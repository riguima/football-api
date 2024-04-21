from itertools import count

from parsel import Selector


def get_rows_of_competition(competition, rows):
    result = []
    for i in count(rows.index(competition) + 1):
        if rows[i].css('.Text.gwfIvP::text').get():
            return result
        result.append(rows[i])


def get_games(driver, games_date, competitions):
    driver.get(f'https://www.sofascore.com/football/{games_date:%Y-%m-%d}')
    while True:
        selector = Selector(driver.page_source)
        rows = selector.css('.Box.klGMtt')
        if rows:
            break
    filtered_competitions = filter(
        lambda c: c.css('.Text.gwfIvP::text').get()
        and c.css('.Text.gwfIvP::text').get().split(',')[0] in competitions,
        rows,
    )
    result = {}
    for competition in filtered_competitions:
        for game in get_rows_of_competition(competition, rows):
            try:
                competition_label = (
                    competition.css('.Text.gwfIvP::text').get('').split(',')[0]
                )
                game_data = {
                    'home': {
                        'name': game.css('.Box.hYFYfq img')[0].attrib['alt'],
                        'goals': int(
                            game.css('.Text.currentScore::text')[0].get()
                        ),
                        'image': game.css('.Box.hYFYfq img')[0]
                        .attrib['src']
                        .replace('/small', ''),
                    },
                    'away': {
                        'name': game.css('.Box.hYFYfq img')[1].attrib['alt'],
                        'goals': int(
                            game.css('.Text.currentScore::text')[1].get()
                        ),
                        'image': game.css('.Box.hYFYfq img')[1]
                        .attrib['src']
                        .replace('/small', ''),
                    },
                }
                if result.get(competition_label):
                    result[competition_label].append(game_data)
                else:
                    result[competition_label] = [game_data]
            except IndexError:
                continue
    return result
