from flask import Blueprint, jsonify, current_app, request
from apis.models.users import User
from apis.services import UserService
from apis.schemas import UserSchema
from collections import defaultdict
from uuid import uuid4
from bson.objectid import ObjectId
from apis.utils.decorator import login_required
from passlib.apps import custom_app_context as pwd_context

user = Blueprint("user", __name__, url_prefix="/users")

user_service = UserService()

@user.route("/", methods=["GET"])
@login_required
def list():
    user = user_service.list()
    return jsonify(user)

@user.route("/<id>/", methods=["PUT"])
@login_required
def update(id):
    data = request.json
    user = User.objects.exclude('password').get(pk=ObjectId(id))
    user.name = data['name']
    user.save()
    return jsonify(user)

@user.route("/<id>/", methods=["GET"])
@login_required
def retrive(id):
    user = User.objects.exclude('password').get(pk=ObjectId(id))
    print(user)
    return jsonify(user)


@user.route("/register/", methods=["POST"])
def register():
    data = UserSchema()
    errors = data.validate(request.json)
    if errors:
        error_list = defaultdict(list)
        for field, value in errors.items():
            error_list[field]=value[0]
        response = dict({"errors": error_list})
        return jsonify(response), 422
    valid_data = data.dump(request.json)
    valid_data["password"] = pwd_context.hash(valid_data["password"])
    user = user_service.create(valid_data)
    user = data.load(user)
    return jsonify(user)

@user.route("/login/", methods=["GET"])
def login():
    data = UserSchema()
    errors = data.validate(request.json)
    if errors:
        error_list = defaultdict(list)
        for field, value in errors.items():
            error_list[field]=value[0]
        response = dict({"errors": error_list})
        return jsonify(response), 422
    valid_data = data.dump(request.json)
    user = user_service.login(valid_data)
    return jsonify(user)

