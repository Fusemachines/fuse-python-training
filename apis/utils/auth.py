from bson.objectid import ObjectId
from apis.models.users import User as user_model

from apis.services.users import UserService
class Auth:
    @staticmethod
    def get_logged_in_user(new_request):
            # get the auth token
            auth_token = new_request.headers.get('Authorization')
            if auth_token:
                resp = UserService.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    user = user_model.objects.get(pk=resp)
                    response_object = {
                        'status': 'success',
                        'data': {
                            'email': user.email,
                            'address': user.address,
                            'name': user.name
                        }
                    }
                    return response_object, 200
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return response_object, 401

    @staticmethod
    def get_access_token(new_request):
        pass