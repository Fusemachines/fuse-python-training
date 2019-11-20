from flask import Blueprint, jsonify

user = Blueprint("user", __name__, url_prefix="/users")

user_list = [{"name": "Adrin", "address": "London"}, {"name": "Jocab", "address": "NY"}]

@user.route("/")
def users():
    return jsonify(user_list)