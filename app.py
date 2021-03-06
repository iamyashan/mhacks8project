from flask import Flask, send_from_directory
from game import Game
import random

app = Flask(__name__, template_folder='views')

active_games = {}

@app.route('/')
def index():
    return send_from_directory('static','home.html')

chars = ['a', 'b', 'c']
@app.route('/create', methods=['POST'])
def create():
    gameid = random.choice(chars)
    while gameid in active_games:
        gameid += random.choice(chars)
    active_games[gameid] = Game()
    return gameid

@app.route('/<path:path>')
def game_page(path):
    return send_from_directory('static','game.html')

if __name__ == '__main__':
    # listen on external IPs
    app.run(host='localhost', port=3000, debug=True)
