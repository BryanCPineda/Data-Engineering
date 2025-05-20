import unittest
from app.utils import validate_email, validate_password

class TestUtils(unittest.TestCase):

    def test_validate_email_valid(self):
        self.assertTrue(validate_email("usuario@example.com"))
        self.assertTrue(validate_email("nombre.apellido@dominio.co"))
        self.assertTrue(validate_email("user123+test@gmail.com"))
        

    def test_validate_email_invalid(self):
        with self.assertRaises(ValueError):
            validate_email("usuarioexample.com")  
        with self.assertRaises(ValueError):
            validate_email("usuario@.com")        
        with self.assertRaises(ValueError):
            validate_email("usuario@dominio")    

    def test_validate_password_valid(self):
        self.assertTrue(validate_password("Password123"))
        self.assertTrue(validate_password("MiClave9Segura"))
        self.assertTrue(validate_password("UnaClave88Fuertes"))

    def test_validate_password_invalid(self):
        with self.assertRaises(ValueError):
            validate_password("short")               
        with self.assertRaises(ValueError):
            validate_password("nouppercase1")        
        with self.assertRaises(ValueError):
            validate_password("NOLOWERCASE1")        
        with self.assertRaises(ValueError):
            validate_password("NoNumbersHere")       

if __name__ == '__main__':
    unittest.main()