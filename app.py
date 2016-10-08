from flask import Flask, send_from_directory
from game import Game
import random

app = Flask(__name__, template_folder='views')

active_games = {}

@app.route('/')
def index():
    return send_from_directory('views','home.html')

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
    app.run(host='localhost', port=3000, debug=True)
