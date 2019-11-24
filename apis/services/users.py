from apis.models import User 

class UserService:
    def create(self, data):
        user = User(**data).save()
        return user

    def list(self):
        return User.objects
