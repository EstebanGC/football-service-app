from flask import Blueprint, jsonify
from app.services.soccer_service import SoccerService

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "message": "Welcome to the football app"
    })

@main.route('/api/leagues')
def get_leagues():
    leagues = SoccerService.get_available_leagues()
    return jsonify(leagues)

@main.route('/api/schedule/<league>/<season>')
def get_league_schedule(league, season):
    data = SoccerService.get_schedule(league, season)
    if not data:
        return jsonify({'error': 'Matches not found'}), 404
    return jsonify(data)