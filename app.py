from flask import Flask, current_app
from game import Game
import random

app = Flask(__name__, template_folder='views')

active_games = {}

@app.route('/')
def index():
    return current_app.send_static_file('index.html')

@app.route('/create', methods=['POST'])
def create():
    gameid = ''
    while gameid == '' or gameid in active_games:
        game.append(c)
    active_games[gameid] = Game()
    return id

@app.route('/<path:path>')
def game_page(path):
    return current_app.send_static_file('game.html')

if __name__ == '__main__':
    # listen on external IPs
    app.run(host='localhost', port=80, debug=True)
