from flask import Blueprint, jsonify, current_app, request
from apis.models.users import User
from apis.services import UserService

user = Blueprint("user", __name__, url_prefix="/users")

user_service = UserService()

@user.route("/", methods=["POST"])
def users():
    data = request.json
    user = user_service.create(**data)
    return jsonify(user)

@user.route("/", methods=["GET"])
def list():
    user = user_service.list()
    return jsonify(user)