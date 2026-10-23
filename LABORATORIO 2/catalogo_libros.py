libros = [
    {
    "Codigo": "111",
    "Titulo": "Cien años de soledad",
    "Autor": "Gabriel García Márquez",
    "Año": 1967,
    },
    {
    "Codigo": "112",
        "Titulo": "El amor en los tiempos del cólera ",
        "Autor": "Gabriel García Márquez",
        "Año": 1985,
    },
    {
    "Codigo": "113",
        "Titulo": "Crónica de una muerte anunciada",
        "Autor": "Gabriel García Márquez",
        "Año": 1981
    } 
]

codigo_libro = input("Ingrese el código del libro que desea consultar: ").strip()

for libro in libros:
    if libro["Codigo"] == codigo_libro:
        libro_encontrado = libro
        break 

if libro_encontrado:
    print("\n¡Libro encontrado!")
    print(f"Título: {libro_encontrado['Titulo']}")
    print(f"Autor: {libro_encontrado['Autor']}")
    print(f"Año de publicación: {libro_encontrado['Año']}")
else:
    print("No se encontró un libro con ese código.")

print("--- AMPLIACIÓN: REGISTRAR NUEVO LIBRO ---")

nuevo_codigo = input("Ingrese el código del nuevo libro: ").strip()

codigo_repetido = False
for libro in libros:
    if libro["Codigo"] == nuevo_codigo:
        codigo_repetido = True
        break

if codigo_repetido:
    print("Error: Ya existe un libro registrado con ese código. No se puede agregar.")
else:

    nuevo_titulo = input("Ingrese el título: ").strip()
    nuevo_autor = input("Ingrese el autor: ").strip()
    nuevo_anio = int(input("Ingrese el año de publicación: "))
    
    nuevo_libro = {
        "Codigo": nuevo_codigo,
        "Titulo": nuevo_titulo,
        "Autor": nuevo_autor,
        "Año": nuevo_anio,
    }
    
    libros.append(nuevo_libro)
    print("¡Libro agregado con éxito!")
    print("Cantidad total de libros en el catálogo:", len(libros))