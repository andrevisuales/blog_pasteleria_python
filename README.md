# Blog de Pastelería
Proyecto personal dedicado a la pastelería, donde documento recetas, técnicas y aprendizajes durante mi formación gastronómica.

En esta etapa, el blog funciona como un programa de Python por consola que permite consultar publicaciones, buscar por título, filtrar por etiquetas y validar la información de los posts.

## Funcionalidades
El programa cuenta con un menú interactivo que permite:

- Ver todas las publicaciones con su título, autor y estado.
- Buscar publicaciones por título.
- Filtrar publicaciones por etiquetas (tags).
- Validar la información de los posts.
- Salir del programa.

## Estructura del proyecto
```text
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Organización de los módulos
- `main.py`: archivo principal que inicia el programa y coordina las opciones del menú.
- `blog/__init__.py`: identifica la carpeta `blog` como un paquete de Python.
- `blog/datos.py`: contiene los datos del autor, las publicaciones, los estados y las etiquetas.
- `blog/menu.py`: muestra el menú interactivo y recibe las opciones del usuario.
- `blog/operaciones.py`: contiene las funciones para listar, buscar y filtrar publicaciones.
- `blog/validaciones.py`: verifica que los datos de las publicaciones sean correctos.

## Cómo ejecutar el programa
1. Tener Python 3 instalado.
2. Abrir la carpeta `blog_consola` en VS Code.
3. Abrir la terminal integrada.
4. Ejecutar el siguiente comando:

```bash
python3 main.py
```

5. Seleccionar una opción del menú interactivo.