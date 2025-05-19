import re

def validate_email(email: str) -> bool:
    """
    Valida el formato de un correo electrónico.
    :param email: Correo electrónico a validar.
    :return: True si el correo es válido, False en caso contrario.
    """
    # Expresión regular para validar el formato del correo electrónico
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        raise ValueError("El correo electrónico no es válido")

def validate_password(password: str) -> bool:
    """
    Valida la fortaleza de una contraseña.
    :param password: Contraseña a validar.
    :return: True si la contraseña es fuerte, False en caso contrario.
    """
    # La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número
    if (len(password) < 8 or
        not re.search(r'[A-Z]', password) or
        not re.search(r'[a-z]', password) or
        not re.search(r'[0-9]', password)):
        raise ValueError("La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número")
    return True