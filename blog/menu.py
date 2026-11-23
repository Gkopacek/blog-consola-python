from blog.operaciones import listar_posts, filtrar_por_tag, buscar_por_titulo
from blog.datos import posts
from blog.validaciones import validar_lista_posts
def iniciar_blog():
    
    while(True):
        print("""--- MENU DEL BLOG ---
        1. Ver todos los posts
        2. Buscar por titulo
        3. Filtrar por tag
        4. Validar posts
        5. Salir""")
        
        try:
            seleccion = input("elegi la opcion del menu: ")
            
            opcion = int(seleccion)       
        
            if(opcion == 1):
                listar_posts(posts)
                    
            elif(opcion == 2):
                
                try:
                
                    titulo_buscado = input("que estas buscando?: ").strip().lower()
                    titulos_encontrados  = buscar_por_titulo(posts, titulo_buscado)
                    
                    if titulos_encontrados:
                        listar_posts(titulos_encontrados)
                    
                    else:
                        print(f"no se encontraron titulos que contengan la palabra o frase {titulo_buscado}")
                except (ValueError, TypeError) as e:
                    print(f"Ocurrio un error: {e}")
                    

            elif(opcion == 3):
                try:        
                    etiqueta_buscada = input("selecciona la etiqueta por la que queres filtrar: ").lower().strip()
                    
                    filtrado_por_tag = filtrar_por_tag(posts, etiqueta_buscada)
                    
                    if(filtrado_por_tag):
                        listar_posts(filtrado_por_tag)
                    else:
                        print(f"no hay coincidencias en la busqueda con '{etiqueta_buscada}'")
                        print('los tags para filtrar son los siguientes: "Java", "Python", "JavaScript", "Django"' )
                except(ValueError, TypeError) as e:
                    print(f"Ocurrio un error: {e}")
            
            elif(opcion == 4):
                
                try:
                    validos, errores = validar_lista_posts(posts)
                    if errores:
                        print("Se encontraron errores:")
                        for r in errores:
                            print(r)
                    else:
                        print(f"Todos los {len(validos)} posts son válidos ✓")
                except (ValueError, TypeError) as e:
                    print(f"Ocurrió un error: {e}")
            
            elif(opcion == 5):
                        print("gracias vuelva pronto")
                        break
            else:print("por favor elegi una opcion valida")
        
        except ValueError:
            print(f"Se esperaba un numero entero")