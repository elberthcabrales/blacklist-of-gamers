from datetime import datetime

from core.main import db


class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50))
    reason = db.Column(db.String(50))
    game_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, reason, game_id):
        self.email = email
        self.reason = reason
        self.game_id = game_id

    def __repr__(self):
        return '{"Email":"%s","Reason":"%s","Game":"%s"}' % (self.email, self.reason, self.game_id)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'reason': self.reason,
            'game_id': self.game_id,
            'timestamp': self.timestamp
        }
