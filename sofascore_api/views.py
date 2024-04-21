from datetime import datetime

from flask import jsonify
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from sofascore_api.api import get_games

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)


def init_app(app):
    @app.get('/games/<date>/<competition>')
    def games(date, competition):
        return jsonify(
            get_games(
                driver, datetime.strptime(date, '%Y-%m-%d'), [competition]
            )
        )
