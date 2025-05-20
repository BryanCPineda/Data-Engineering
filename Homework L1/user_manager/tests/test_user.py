import unittest
from app.user import User  # ajusta el import si tu estructura es diferente


class TestUser(unittest.TestCase):
    
    def test_user_creation(self):
        user = User(name="Juan", email="juan@test.com", password="Password123")
        self.assertEqual(user.name, "Juan")
        self.assertEqual(user.email, "juan@test.com")
        self.assertEqual(user.password, "Password123")
        self.assertIsInstance(user.id, str)

    def test_user_to_dict(self):
        user = User(name="Ana", email="ana@test.com", password="Secure123")
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['name'], "Ana")
        self.assertEqual(user_dict['email'], "ana@test.com")
        self.assertEqual(user_dict['password'], "Secure123")
        self.assertEqual(user_dict['id'], user.id)

    def test_user_from_dict(self):
        data = {
            'id': '1234-5678-uuid',
            'name': 'Carlos',
            'email': 'carlos@test.com',
            'password': 'Abc12345'
        }
        user = User.from_dict(data)

        self.assertEqual(user.id, '1234-5678-uuid')
        self.assertEqual(user.name, 'Carlos')
        self.assertEqual(user.email, 'carlos@test.com')
        self.assertEqual(user.password, 'Abc12345')

    def test_unique_id_generation(self):
        user1 = User(name="U1", email="u1@test.com", password="Pass1")
        user2 = User(name="U2", email="u2@test.com", password="Pass2")
        self.assertNotEqual(user1.id, user2.id)