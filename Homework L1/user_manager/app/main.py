"""
Módulo Principal de la Aplicación de Gestión de Usuarios

Este módulo proporciona una interfaz de línea de comandos para gestionar registros de usuarios. Permite:
- Registrar nuevos usuarios
- Listar usuarios registrados
- Buscar usuarios por nombre
- Eliminar usuarios
- Guardar y cargar datos de usuarios

La aplicación utiliza colorama para colorear el texto en terminal e interactúa con UserManager
para realizar operaciones relacionadas con usuarios.

Funciones:
    menu(): Muestra las opciones del menú principal
    main(): Ejecuta el bucle principal de la aplicación manejando las interacciones del usuario

Dependencias:
    - UserManager del módulo manager
    - User del módulo user
    - validate_email, validate_password del módulo utils
    - colorama para el formato de texto en terminal
"""
import os
from app.manager import UserManager
from app.user import User
from app.utils import validate_email, validate_password
from colorama import Fore, Back, init

init(autoreset=True)  # Inicializa colorama para que los colores se reinicien automáticamente

print(Fore.CYAN + "Bienvenido al sistema de gestión de usuarios")

'''
menu(): Muestra las opciones del menú principal
'''
def menu():
    print(Fore.YELLOW + "1. Registrar un nuevo usuario")
    print(Fore.YELLOW + "2. Listar usuarios registrados")
    print(Fore.YELLOW + "3. Buscar usuario por nombre")
    print(Fore.YELLOW + "4. Eliminar un usuario")
    print(Fore.YELLOW + "5. Guardar")
    print(Fore.YELLOW + "6. Salir")

'''
main(): Ejecuta el bucle principal de la aplicación manejando las interacciones del usuario
'''

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear') 

def main():
    manager = UserManager()
    manager.load_users()  

    while True:
        print(Fore.CYAN + "\nSeleccione una de las siguientes opciones:")
        menu()
        choice = input(Fore.GREEN + "Opción: ")
        clear_console()
        if choice == '1':
            name = input(Fore.MAGENTA + "Ingrese el nombre del usuario: ").lower()
            email = input(Fore.MAGENTA + "Ingrese el correo electrónico: ").lower()
            print(Fore.CYAN + "La contraseña debe tener al menos 8 caracteres" + "\nLa contraseña debe contener al menos una letra mayúscula" + "\nLa contraseña debe contener al menos una letra minúscula" + "\nLa contraseña debe contener al menos un número")
            password = input(Fore.MAGENTA + "Ingrese la contraseña: ")

            try:
                validate_email(email)
                validate_password(password)
                manager.add_user(User(name, email, password))
                print(Fore.GREEN + "Usuario registrado exitosamente")
            except ValueError as error:
                print(Fore.RED + str(error))

        elif choice == '2':
            users = manager.list_users()
            if not users:
                print(Fore.RED + "No hay usuarios registrados")
            else:
                print(Fore.MAGENTA + "Usuarios registrados:")
                for user in users:
                    print(Fore.CYAN + f"Nombre: {Fore.GREEN + user.name}" + Fore.CYAN + f", Correo: { Fore.GREEN + user.email}")
            
        elif choice == '3':
            name = input(Fore.MAGENTA + "Ingrese el nombre del usuario a buscar: ")
            users = manager.find_user(name)
            if not users:
                print(Fore.RED + "No se encontraron usuarios con ese nombre")
            else:
                print(Fore.GREEN + "Usuarios encontrados:")
                for user in users:
                    print(Fore.CYAN + f"Nombre: {Fore.GREEN + user.name}" + Fore.CYAN + f", Correo: { Fore.GREEN + user.email}")
        
        elif choice == '4':
            email = input(Fore.MAGENTA + "Ingrese el correo electrónico del usuario a eliminar: ")
            try:
                manager.delete_user(email)
                print(Fore.RED + "Usuario eliminado exitosamente")
            except ValueError as error:
                print(Fore.RED + str(error))
        
        elif choice == '5':
            manager.save_users()
            print(Back.GREEN + "Usuarios guardados exitosamente")
        
        elif choice == '6':
            manager.save_users()
            print(Fore.GREEN + "Saliendo del programa...")
            break
        
        else:
            print(Fore.RED + "Opción no válida, por favor intente de nuevo")

if __name__ == "__main__":
    main()
