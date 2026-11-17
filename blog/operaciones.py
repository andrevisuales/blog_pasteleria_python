from blog.validaciones import validar_post


# Función para listar posts
def listar_posts(lista):
    print("Lista de posts")
    for post in lista:
        es_valido, mensaje = validar_post(post)

        if es_valido:
            print(f"- {post['titulo']} | Autor: {post['autor']['nombre']} | Estado: {post['estado']}")
        else:
            if isinstance(post, dict):
                titulo = post.get("titulo", "Sin título")
                autor = post.get("autor", {})
                estado = post.get("estado", "Sin estado")

                if isinstance(autor, dict):
                    nombre_autor = autor.get("nombre", "Sin autor")
                else:
                    nombre_autor = "Sin autor"

                print(f"- {titulo} | Autor: {nombre_autor} | Estado: {estado} | Datos incompletos")
            else:
                print("Publicación con datos incompletos")

# Función para buscar posts por título
def buscar_por_titulo(lista, termino):
    resultado =[]

    for post in lista:
        if isinstance(post, dict):
            titulo = post.get("titulo", "")
            if isinstance(titulo, str):
                if termino.lower() in titulo.lower():
                    resultado.append(post)
    return resultado

# Función para filtrar posts por tag
def filtrar_por_tag(lista, tag):
    resultado = []

    for post in lista:
        if isinstance(post, dict):
            etiquetas = post.get("tags", [])
            if isinstance(etiquetas, list):
                for etiqueta in etiquetas:
                    if isinstance(etiqueta, str):
                        if tag.lower() == etiqueta.lower():
                            resultado.append(post)
    return resultado