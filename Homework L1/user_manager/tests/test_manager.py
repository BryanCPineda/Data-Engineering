import unittest
import tempfile
import os
import json
from app.manager import UserManager
from app.user import User

class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()

        self.manager = UserManager()
        self.manager.file_path = self.temp_file.name

        self.user1 = User("Alice", "alice@example.com", "Password123")
        self.user2 = User("Bob", "bob@example.com", "Password456")

    def tearDown(self):
        os.unlink(self.temp_file.name)

    def test_add_user(self):
        self.manager.add_user(self.user1)
        self.assertEqual(len(self.manager.users), 1)
        self.assertEqual(self.manager.users[0].email, "alice@example.com")

    def test_add_duplicate_user_raises(self):
        self.manager.add_user(self.user1)
        with self.assertRaises(ValueError):
            self.manager.add_user(User("Alice2", "alice@example.com", "OtherPass"))

    def test_list_users(self):
        self.manager.add_user(self.user1)
        self.manager.add_user(self.user2)
        users = self.manager.list_users()
        self.assertEqual(len(users), 2)

    def test_find_user(self):
        self.manager.add_user(self.user1)
        result = self.manager.find_user("alice")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Alice")

    def test_delete_user(self):
        self.manager.add_user(self.user1)
        self.manager.delete_user("alice@example.com")
        self.assertEqual(len(self.manager.users), 0)

    def test_delete_user_not_found_raises(self):
        with self.assertRaises(ValueError):
            self.manager.delete_user("nonexistent@example.com")

    def test_save_and_load_users(self):
        self.manager.add_user(self.user1)
        self.manager.add_user(self.user2)
        self.manager.save_users()

        # Cargar en una nueva instancia para verificar persistencia
        new_manager = UserManager()
        new_manager.file_path = self.temp_file.name
        new_manager.load_users()
        self.assertEqual(len(new_manager.users), 2)
        self.assertEqual(new_manager.users[1].email, "bob@example.com")

if __name__ == '__main__':
    unittest.main()