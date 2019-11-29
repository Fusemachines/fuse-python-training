from apis.models import User
from flask_marshmallow.schema import Schema
from flask_marshmallow.fields import fields

class UserSchema(Schema):
    email = fields.Email(required=True)
    name = fields.String()
    address = fields.String()
    password = fields.String(load_only=True)