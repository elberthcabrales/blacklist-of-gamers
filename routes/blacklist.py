from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services.blacklist import BlacklistService
from validators.AddToBlacklistValidator import AddToBlacklistValidator

bp = Blueprint('blacklist', __name__)


@bp.route('/blacklist', methods=['POST'])
@swag_from('doc/add_to_blacklist.yml')
def add_to_blacklist():
    try:
        AddToBlacklistValidator(request.form).validate()
        email = request.json['email']
        reason = request.json['reason']
        game_id = request.json['game_id']
        BlacklistService().add_user(email, reason, game_id)
    except Exception as e:
        return str(e), 500
    return 'Blacklist added successfully', 200


@bp.route('/blacklist/check', methods=['POST'])
@swag_from('doc/blacklist_check.yml')
def check_blacklist():
    email = request.json['email']
    if email is None:
        return 'Email is required', 400
    try:
        return jsonify(BlacklistService().check_blacklist(email)), 200
    except Exception as e:
        return str(e), 500


@bp.route('/check-health', methods=['GET'])
def check_health():
    request.logger.info('Health check')
    return 'Ok', 200


@bp.route('/tos', methods=['GET'])
def terms():
    return 'By using the API, you agree to the terms and conditions.', 200