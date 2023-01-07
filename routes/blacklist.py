from flask import Blueprint, request
from flasgger import swag_from

bp = Blueprint('blacklist', __name__)


@bp.route('/blacklist', methods=['POST'])
@swag_from('doc/add_to_blacklist.yml')
def add_to_blacklist():
    return 'Success', 201


@bp.route('/blacklist/check', methods=['POST'])
@swag_from('doc/blacklist_check.yml')
def check_blacklist():
    return 'check blacklist', 200


@bp.route('/check-health', methods=['GET'])
def check_health():
    request.logger.info('Health check')
    return {'state': 'Ok'}, 200


@bp.route('/tos', methods=['GET'])
def terms():
    return 'By using the API, you agree to the terms and conditions.', 200