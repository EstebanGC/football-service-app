from app import db

class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    teams = db.relationship('Team', backref='league')

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'))