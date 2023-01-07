from app import db


class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    reason = db.Column(db.String(50))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

    def __init__(self, email, reason, game_id):
        self.email = email
        self.reason = reason
        self.game_id = game_id

    def __repr__(self):
        return '{"Email":"%s","Reason":"%s","Game":"%s"}' % (self.email, self.reason, self.game_id)
