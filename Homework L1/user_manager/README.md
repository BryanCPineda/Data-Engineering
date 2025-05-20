# Sistema de Gestión de Usuarios

Esta es una aplicación de consola en Python para gestionar usuarios: registrar, listar, buscar y eliminar usuarios con validaciones de correo y contraseña. Los usuarios se almacenan en un archivo JSON.

---

## Tecnologías usadas

- Python 3.x
- Librería `colorama` para colores en consola
- Librería `python-decouple` (opcional, si usas variables de entorno)
- Módulo `re` para validaciones con expresiones regulares

---

## Requisitos

- Tener Python 3 instalado ([Descargar Python](https://www.python.org/downloads/))
- Crear y activar un entorno virtual (recomendado)
- Instalar las dependencias usando `pip`

---

## Instalación y configuración

1. Clonar o descargar el repositorio

```
git clone https://github.com/BryanCPineda/Data-Engineering.git
cd tu_repositorio
```

2. Crear entorno virtual

```
python -m venv venv
```

3. Activar entorno virtual

- En Windows (cmd):

```
venv\Scripts\activate
```

- En Linux/MacOS:

```
source venv/bin/activate
```

4. Instalar dependencias

```
pip install -r requirements.txt
```

Uso

Antes de ejecutar la aplicación, es recomendable configurar las variables de entorno. Debes crear un archivo `.env` en la raíz del proyecto y definir las variables necesarias.

```
DATA = data/users.json
```

Para ejecutar la aplicación, desde la terminal activa (y en el entorno virtual si usas):

```
python -m app.main
```

Verás un menú interactivo con opciones para:

- Registrar un nuevo usuario
- Listar usuarios registrados
- Buscar usuario por nombre
- Eliminar un usuario
- Guardar usuarios en archivo JSON
- Salir de la aplicación

Validaciones

- Correo electrónico: Debe tener formato válido (ejemplo: usuario@dominio.com)
- Contraseña: Debe tener al menos 8 caracteres, incluir una letra mayúscula, una minúscula y un número.

Estructura del proyecto

```
.
├── app
│ ├── main.py # Punto de entrada del programa
│ ├── manager.py # Lógica para manejar usuarios y persistencia
│ ├── user.py # Clase User que representa un usuario
│ └── utils.py # Funciones de validación y utilidades
├── users.json # Archivo donde se guardan los usuarios
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación del proyecto
```

## Testing automatizado de la aplicación de gestión de usuarios

Esta aplicacion cuenta con testing automatizado, para ejecutarlo se debe correr el siguiente comando:

```
python -m unittest discover -s tests
```

## Autor

BryanCPineda

## Licencia

MIT License
