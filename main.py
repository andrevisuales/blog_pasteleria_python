from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


# Menú interactivo
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        # interacciones - Mostrar las publicaciones
        if opcion == 1:
            listar_posts(posts)

        #Interacciones - Buscar por título
        elif opcion == 2:
            buscar = input("Buscar por el título: ").strip()

            if buscar == "":
                print("Tenés que ingresar un título para buscar")
            else:
                resultado = buscar_por_titulo(posts,buscar)
                if resultado:
                    for post in resultado:
                        print("-", post["titulo"])
                else:
                    print("No se encontraron publicaciones con ese título.")

        #Interacciones - Filtrar por etiqueta/tag
        elif opcion == 3:
            tag_buscar = input("Filtrar por tag: ").strip()

            if tag_buscar == "":
                print("Tenés que ingresar el nombre de un tag para buscar")
            else:
                resultado = filtrar_por_tag(posts, tag_buscar)
                if resultado:
                    for post in resultado:
                        print("-", post["titulo"])
                else:
                    print("No se encontraron publicaciones con ese tag")

        # Interacciones - Validar posts
        elif opcion == 4:
            for post in posts:
                es_valido, mensaje = validar_post(post)

                if isinstance(post, dict):
                    id_post = post.get("id", "sin ID")
                else:
                    id_post = "sin ID"

                if es_valido:
                    print(f"Post {id_post}: válido")
                else:
                    print(f"Post {id_post}: {mensaje}")

        #Interacciones - Salir del menú
        elif opcion == 5:
            print("¡Gracias por visitar nuestro blog de Pastelería!")
            break
        
        #Interacciones - Opciones inválidas
        else:
            print("Opción inválida, intenta de nuevo")