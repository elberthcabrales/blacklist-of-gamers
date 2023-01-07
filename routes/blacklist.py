from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services.blacklist import BlacklistService

bp = Blueprint('blacklist', __name__)


@bp.route('/blacklist', methods=['POST'])
@swag_from('doc/add_to_blacklist.yml')
def add_to_blacklist():
    try:
        blacklist_service = BlacklistService(request)
        blacklist_service.add_user()
    except Exception as e:
        return str(e), 500
    return 'Blacklist added successfully', 200


@bp.route('/blacklist/check', methods=['POST'])
@swag_from('doc/blacklist_check.yml')
def check_blacklist():
    try:
        blacklist_service = BlacklistService(request)
        reports = blacklist_service.check_blacklist()

        return jsonify(reports), 200
    except Exception as e:
        return str(e), 500


@bp.route('/check-health', methods=['GET'])
def check_health():
    request.logger.info('Health check')
    return 'Ok', 200


@bp.route('/tos', methods=['GET'])
def terms():
    return 'By using the API, you agree to the terms and conditions.', 200