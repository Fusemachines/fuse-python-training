import datetime
from flask import jsonify, current_app

from bson.objectid import ObjectId
import jwt
from apis.models import User 

from passlib.apps import custom_app_context as pwd_context

JWT_SECRET_KEY ="my-temp-jwt-secret-key"


class UserService:
    def create(self, data):
        user = User(**data).save()
        return user

    def list(self):
        return User.objects.exclude('password')
    
    def match_password(self, db_password, query_password):
        if pwd_context.verify(db_password, query_password):
            return True
        return False

    def login(self, data):
        email = data["email"]
        password = data["password"]

        user_db = User.objects(email=email)[0]
        password_matches = self.match_password(password, user_db["password"])
        if password_matches:
            token = self.encode_auth_token(user_db["id"])
            return {"idToken" :  token}
        else:
            return "Username/Password didn't match."

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'user_id': str(user_id),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
            }
            refresh_payload = {
                'user_id': str(user_id),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }


            access_token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256').decode('utf-8')
            refresh_token = jwt.encode(refresh_payload, JWT_SECRET_KEY, algorithm='HS256').decode('utf-8')
            return {'access_token':access_token, "refresh_token":refresh_token}

        except Exception as e:
            return e
    
    @staticmethod  
    def decode_auth_token(auth_token):
            """
            Decodes the auth token
            :param auth_token:
            :return: integer|string
            """
            try:
                payload = jwt.decode(auth_token.split(" ")[-1], JWT_SECRET_KEY)
                return ObjectId(payload['user_id'])
            except jwt.ExpiredSignatureError:
                return 'Signature expired. Please log in again.'
            except jwt.InvalidTokenError:
                return 'Invalid token. Please log in again.'
