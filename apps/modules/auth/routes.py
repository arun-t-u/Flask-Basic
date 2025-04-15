from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from apps.modules.models import User, StatusEnum, Institution


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/test', methods=['POST'])
def test():
    return jsonify({"message": "Test successful"}), 200