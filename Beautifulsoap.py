import requests
from bs4 import Beautifulsoap


url = 'http://portal.abu.edu.ng/'
page = requests.get(url)

soup = Beautifulsoap(page.text, 'html.parser')
games = soup.select("._ys_6mtdyh")
for game in games:
    print(game.get_text())