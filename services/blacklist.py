from models.blacklistModel import Blacklist
from datetime import datetime, timedelta

from core.main import db


class BlacklistService(object):
    def add_user(self, email, reason, game_id):

        blacklist = Blacklist(email, reason, game_id)
        db.session.add(blacklist)
        db.session.commit()

    def check_blacklist(self, email):
        past_90_days = datetime.utcnow() - timedelta(days=90)
        # filter blacklist by email and timestamp (last 90 days)
        blacklist = Blacklist.query.filter(Blacklist.email == email, Blacklist.timestamp >= past_90_days).all()
        recent_reports = [b.to_dict() for b in blacklist]

        # Count the number of times each reason was reported
        reason_counts = {}
        for r in recent_reports:
            if r['reason'] in reason_counts:
                reason_counts[r['reason']] += 1
            else:
                reason_counts[r['reason']] = 1

        # Get the most commonly reported reason
        most_common_reason = max(reason_counts, key=reason_counts.get)

        # Get the number of games where the player has ever been reported
        game_ids = set([r['game_id'] for r in recent_reports])
        num_reported_games = len(game_ids)

        return {
            'most_common_reason': most_common_reason,
            'num_reports_in_past_90_days': len(recent_reports),
            'num_reported_games': num_reported_games
        }