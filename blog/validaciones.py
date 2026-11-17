from blog.datos import estados_post


# Función para validar los posts
def validar_post(post):
    if not isinstance(post, dict):
        return False, "El post no es un diccionario"
    if "titulo" not in post:
        return False, "Falta la clave título"
    if "contenido" not in post:
        return False, "Falta la clave contenido"
    if "id" not in post:
        return False, "Falta la clave id"
    if "autor" not in post:
        return False, "Falta la clave autor"
    if "tags" not in post:
        return False, "Falta la clave tags"
    if "estado" not in post:
        return False, "Falta la clave estado"
    if not isinstance(post["titulo"], str):
        return False, "El título debe ser un texto"
    if not isinstance(post["contenido"], str):
        return False, "El contenido debe ser un texto"
    if post["titulo"].strip() == "":
        return False, "El título está vacío"
    if post["contenido"].strip() == "":
        return False, "El contenido está vacío"
    if not isinstance(post["autor"], dict):
        return False, "El autor debe ser un diccionario"
    if "nombre" not in post["autor"]:
        return False, "Falta el nombre del autor"
    if not isinstance(post["autor"]["nombre"], str):
        return False, "El nombre del autor debe ser un texto"
    if post["autor"]["nombre"].strip() == "":
        return False, "El nombre del autor está vacío"
    if not isinstance(post["tags"], list):
        return False, "Los tags deben ser una lista"
    for tag in post["tags"]:
        if not isinstance(tag, str):
            return False, "Cada tag debe ser un texto"
        if tag.strip() == "":
            return False, "Los tags no pueden estar vacíos"
    if post["estado"] not in estados_post:
        return False, "El estado del post no es válido"
    return True, "Post válido"