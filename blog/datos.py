perfil_autor = {
   "nombre": "Victoria Bach",
   "bio": "Estudiante de Pasteleria",
   "especialidad": "Pastelería clásica y moderna",
   "redes_sociales": ["@vickych", "@vicky_bach"]
}
# Estados posibles y etiquetas 
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Recetas", "Técnicas", "Dificultad"}

# Lista de publicaciones 
posts = [
   {"id" : 1,
    "titulo" : "Mi primera torta de chocolate",
    "autor" : perfil_autor,
    "categoría" : "Recetas",
    "contenido" : "Mi primera torta de chocolate fue todo un desafío. Desde preparar la mezcla hasta controlar el tiempo de horneado, cada paso fue un aprendizaje.",
    "tags" : ["Chocolate", "Tortas", "pasteleria"],
    "estado" : "publicado"
   },
   {"id" : 2,
    "titulo" : "Cómo preparar crema pastelera",
    "autor" : perfil_autor,
    "categoría" : "Técnicas",
    "contenido" : "La crema pastelera es una preparación básica y muy versátil en pastelería. En esta entrada explico los ingredientes, el procedimiento y algunos consejos para conseguir una textura suave y sin grumos.",
    "tags" : ["Cremas", "pasteleria", "rellenos"],
    "estado" : "borrador"
   },
   {"id" : 3,
    "titulo" : "Mis primeros pasos en pastelería",
    "autor" : perfil_autor,
    "categoría" : "Dificultad",
    #"contenido" : "Comenzar a estudiar pastelería me permitió descubrir un mundo de técnicas, ingredientes y sabores.",
    "contenido" : "",
    "tags" : ["pasteleria", "rellenos"],
    #"tags": "pasteleria",
    "estado" : "archivado"
   }
]
