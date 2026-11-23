
def validar_lista_posts(lista):
    if not isinstance(lista, list):
        raise TypeError("validar_lista_posts solo acepta listas.")

    reportes = []
    posts_validados = []

    for i, post in enumerate(lista):
        try:
            validar_posts(post)
            posts_validados.append(post)
        except (TypeError, ValueError) as e:
            
            id_post = post.get("id", "Sin ID") if isinstance(post, dict) else "N/A"
            reportes.append(f"❌ Post en posición {i} (id={id_post}): {e}")

    return posts_validados, reportes


def validar_posts(post):
  estados_post = ("borrador", "publico", "archivado")
  claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
  clave_obligatoria_autor = "nombre"
  if not isinstance(post, dict):
      raise TypeError("el post debe tener la estructura de un diccionario")
  
  for clave in claves_obligatorias:
        if clave not in post:
            raise ValueError(f"Falta la clave obligatoria '{clave}'")
  
  if not isinstance(post.get("autor"), dict):
      raise TypeError("el autor debe tener la estructura de un diccionario")
  if not isinstance(post.get("tags"), list):
      raise TypeError("el valor tags debe tener la estructura de una lista")
  
  titulo = post.get("titulo")
  contenido = post.get("contenido")

  if not isinstance(titulo, str):
      raise TypeError("el titulo debe ser una cadena de texto")
  if not titulo.strip():
      raise ValueError("el titulo no puede estar vacio ni ser solo espacios")
  if not isinstance(contenido, str):
      raise TypeError("el contenido debe ser una cadena de texto")
  if not contenido.strip():      
      raise ValueError("el contenido no puede estar vacio ni ser solo espacios")

  if post.get("estado") not in estados_post:
      raise ValueError(f"Estado '{post.get('estado')}' inválido. Opciones: {estados_post}")

  if clave_obligatoria_autor not in post.get('autor'):
      raise ValueError(f"falta la clave obligatoria '{clave_obligatoria_autor}'")

  return True