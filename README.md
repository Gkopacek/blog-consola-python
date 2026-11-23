# Sistema de Gestión de Blog por Consola
Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python para la gestión, búsqueda, filtrado y validación de publicaciones de un blog.
La arquitectura del proyecto está estructurada de forma modular mediante paquetes y módulos independientes, separando la interfaz de usuario, la lógica de negocio, las reglas de validación y los datos iniciales.
---
## 📁 Estructura del Proyecto
```text
mi_blog/
│
├── blog/
│   ├── __init__.py          # Inicializador del paquete blog
│   ├── datos.py             # Datos base, constantes y perfiles iniciales
│   ├── validaciones.py      # Funciones de validación de esquemas y tipos
│   ├── operaciones.py       # Funciones de listado, búsqueda y filtrado
│   └── menu.py              # Interfaz de usuario por consola e inputs
│
├── main.py                  # Punto de entrada principal de la aplicación
└── README.md                # Documentación del proyecto
🧩 Descripción de Módulos
blog/datos.py: Almacena las estructuras de datos base (posts, perfil_autor, etiquetas_blog, estados_post).
blog/validaciones.py: Contiene la lógica estricta para validar que cada post cumpla con los tipos de datos, claves obligatorias, estados permitidos y contenido no vacío (validar_posts y validar_lista_posts).
blog/operaciones.py: Aloja las operaciones de lectura y consulta sobre las listas de posts (listar_posts, buscar_por_titulo y filtrar_por_tag).
blog/menu.py: Gestiona la interacción con el usuario mediante la consola, controlando las opciones seleccionadas, la captura de input() y el manejo de excepciones.
main.py: Punto de entrada de ejecución que inicia el ciclo principal del menú.
🚀 Requisitos y Ejecución
Requisitos previos
Python 3.8 o superior instalado en el sistema.
Instrucciones para ejecutar
Clonar el repositorio o descargar la carpeta del proyecto:

bash


Ejecutar el script principal desde la raíz del proyecto:

bash


📋 Funcionalidades del Menú
Ver todos los posts: Lista todos los artículos disponibles mostrando título y autor.
Buscar por título: Permite realizar búsquedas parciales por coincidencia de texto (mínimo 3 caracteres).
Filtrar por tag: Filtra las publicaciones que coincidan con una etiqueta o tecnología específica.
Validar posts: Ejecuta las reglas de validación sobre toda la lista de posts e informa si están correctos o el detalle puntual de los errores encontrados.
Salir: Finaliza la ejecución del programa.


---
### Pasos finales para la entrega:
1. Asegurate de crear el archivo `README.md` en la misma carpeta donde está `main.py`.
2. Hacé el commit y push a tu repositorio de GitHub:
   ```bash
   git add .
   git commit -m "feat: organizacion modular del blog y documentacion readme"
   git push origin main
Verificá que el repositorio esté en modo Público para que los evaluadores puedan revisarlo.