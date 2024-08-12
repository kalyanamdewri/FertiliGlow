from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    cycle_length = db.Column(db.Integer)
    last_period = db.Column(db.String(10))
    points = db.Column(db.Integer, default=0)
    badges = db.relationship('Badge', backref='user', lazy='dynamic')
    logs = db.relationship('Log', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.name}>'

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(64))
    temperature = db.Column(db.Float)
    notes = db.Column(db.String(200))
    diet = db.Column(db.String(200))  # New field for diet
    exercise = db.Column(db.String(200))  # New field for exercise
    sleep_hours = db.Column(db.Float)  # New field for sleep
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Log {self.timestamp}>'


class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    points = db.Column(db.Integer)

    def __repr__(self):
        return f'<Challenge {self.name}>'

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Badge {self.name}>'
