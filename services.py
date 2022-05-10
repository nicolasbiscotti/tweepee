from models import User

class UserService:
  @staticmethod
  def create_user(username):
    return User.create(username=username)
