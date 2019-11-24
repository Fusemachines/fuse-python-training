from flask import Blueprint, jsonify, current_app, request
from apis.models.users import User
from apis.services import UserService
from apis.schemas import UserSchema
from collections import defaultdict

user = Blueprint("user", __name__, url_prefix="/users")

user_service = UserService()

@user.route("/", methods=["POST"])
def users():
    data = UserSchema()
    errors = data.validate(request.json)
    if errors:
        error_list = defaultdict(list)
        for field, value in errors.items():
            error_list[field]=value[0]
        response = dict({"errors": error_list})
        return jsonify(response), 422
    valid_data = data.dump(request.json)
    user = user_service.create(valid_data)
    return jsonify(user)

@user.route("/", methods=["GET"])
def list():
    user = user_service.list()
    return jsonify(user)