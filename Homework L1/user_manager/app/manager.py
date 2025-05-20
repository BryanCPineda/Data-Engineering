"""
La clase UserManager administra una colección de objetos User con métodos para agregar, listar, buscar y eliminar usuarios.

Esta clase proporciona funcionalidades para:
- Agregar nuevos usuarios con direcciones de correo electrónico únicas
- Listar todos los usuarios actuales
- Buscar usuarios por nombre
- Eliminar usuarios por correo electrónico
- Guardar usuarios en un archivo JSON
- Cargar usuarios desde un archivo JSON

Atributos:
    users (list): Una lista de objetos User actualmente gestionados
    file_path (str): Ruta al archivo JSON para almacenar datos de usuarios, cargada desde la configuración del entorno

Métodos:
    list_users(): Devuelve la lista actual de usuarios
    add_user(user): Agrega un nuevo usuario, lanzando un error si el correo electrónico ya existe
    find_user(name): Encuentra usuarios que coincidan con un nombre dado (sin distinguir mayúsculas/minúsculas)
    delete_user(email): Elimina un usuario por su dirección de correo electrónico
    save_users(): Serializa y guarda usuarios en un archivo JSON
    load_users(): Carga usuarios desde un archivo JSON, manejando posibles errores de archivo o análisis
"""

import json 
from decouple import config 
from app.user import User 
import os 
class UserManager:
    def __init__(self):
        self.users = []
        self.file_path = config("DATA")

    def list_users(self):
        return self.users

    def add_user(self, user: User):
        if any(usuario.email == user.email for usuario in self.users):
            raise ValueError(f"El usuario con el correo {user.email} ya existe") 
        self.users.append(user)
    
    def find_user(self, name: str):
      return [usuario for usuario in self.users if name.lower() in usuario.name.lower()]
    
    def delete_user(self, email: str):
      if not any(usuario.email == email for usuario in self.users):
        raise ValueError("Correo electrónico no encontrado")
      else:
        self.users = [usuario for usuario in self.users if usuario.email != email]
    
    def save_users(self):
      with open(self.file_path, 'w') as file:
        json.dump( [usuario.to_dict() for usuario in self.users], file, indent=4)
    
    def load_users(self):
      try:
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
          with open(self.file_path, 'r') as file: 
            data = json.load(file)
            self.users = [User.from_dict(usuario) for usuario in data]
        else:
          self.users = []
      except (FileNotFoundError, json.JSONDecodeError):
        self.users = []



