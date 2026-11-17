def mostrar_menu():
    print()
    print("--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    print()

    try:
        opcion = int(input("Elegí una opción:  ").strip())
        return opcion
    except ValueError:
        print("Error: Por favor, ingresá un número.")
        return 0
    