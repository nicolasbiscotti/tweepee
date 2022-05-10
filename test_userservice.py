from main import create_tables, drop_tables
from models import User
from services import UserService
import unittest

class TestCreateUser(unittest.TestCase):

  def test_should_return_a_user_with_username_nicolas45(self):
    nicolas = UserService.create_user("nicolas45")
    self.assertTrue(isinstance(nicolas, User))
    self.assertEqual('nicolas45', nicolas.username)

if __name__ == '__main__':
  drop_tables()
  create_tables()
  unittest.main()  # pragma: no cover
