"""
Representa un usuario con información básica y métodos de utilidad para serialización.

Esta clase encapsula los detalles del usuario y proporciona métodos para convertir
entre objetos User y representaciones en forma de diccionario.

Atributos:
    name (str): El nombre completo del usuario.
    email (str): La dirección de correo electrónico del usuario.
    password (str): La contraseña del usuario.

Métodos:
    to_dict(): Convierte el objeto User a un diccionario.
    from_dict(data): Crea un objeto User a partir de un diccionario.
"""
import uuid

class User:
  def __init__(self, name: str, email: str, password: str, id=None):
    self.id = id if id is not None else str(uuid.uuid4())
    self.name = name
    self.email = email
    self.password = password

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'password': self.password
    }
  
  @staticmethod
  def from_dict(data: dict):
      return User(
          id=data['id'],
          name=data['name'],
          email=data['email'],
          password=data['password']
      )


