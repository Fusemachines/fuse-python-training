from flask import Blueprint, jsonify, current_app, request
from apis.models.users import User
user = Blueprint("user", __name__, url_prefix="/users")

@user.route("/", methods=["POST"])
def users():
    data = request.json
    user = User(**data)
    user.save()
    return jsonify(user)


@user.route("/", methods=["GET"])
def list():
    user = User.objects
    return jsonify(user)