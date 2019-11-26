from apis.db import db

class User(db.Document):
    email = db.StringField(required=True)
    name = db.StringField(max_length=50)
    address = db.StringField(max_length=50)