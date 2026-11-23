def listar_posts(lista):
    if not isinstance(lista, list):
        raise TypeError("la funcion listar_posts solo acepta listas")
    if(len(lista) > 0):
        for post in lista:
            if not isinstance(post, dict):
                raise TypeError("el post debe ser de tipo diccionario")
            nombre_post = post.get('titulo',"sin titulo")
            datos_autor = post.get('autor', {})
            nombre_autor = datos_autor.get('nombre', "sin nombre de autor")
            
            print(f"nombre del post: {nombre_post} | autor: {nombre_autor}")
    else: raise ValueError("la lista debe contener al menos un post")
            
def buscar_por_titulo(lista, termino):

    if not isinstance(lista, list):
        raise TypeError("buscar por titulo. solo acepta listas")
    if not isinstance(termino, str):
        raise TypeError(f"el dato {termino} es distinto de string")
    termino_en_minusculas = termino.lower().strip()
    if len(termino_en_minusculas) < 3:
        raise ValueError(f"la palabra que busques debe tener al menos 3 letras tu palabra tiene {len(termino_en_minusculas)}")
   
    lista_de_coincidencias = []
    for post in lista:
        if isinstance(post, dict):
            nombre_titulo = post.get('titulo', "")
            if isinstance(nombre_titulo, str):
                nombre_titulo_minusculas  = nombre_titulo.lower().strip()
                if termino_en_minusculas in nombre_titulo_minusculas:
                    lista_de_coincidencias.append(post)

    return lista_de_coincidencias



def filtrar_por_tag(lista, tag):
    
    if not isinstance(lista, list):
        raise TypeError(f"la funcion filtrar_por_tag. solo acepta listas")
    if not isinstance(tag, str):
        raise TypeError(f"el dato {tag} es distinto de string")
    post_con_tag = []
    tag_buscado = tag.lower().strip()
    for post in lista:
        if isinstance(post, dict):
            tags_del_post = post.get("tags", [])
            if isinstance(tags_del_post, (list, set, tuple)):
                tags_normalizados = {t.lower().strip() for t in tags_del_post if isinstance(t, str)}
                
                if tag_buscado in tags_normalizados:
                    post_con_tag.append(post)
    return post_con_tag