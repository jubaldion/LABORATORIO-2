productos = [
    {"codigo": "P001", "nombre": "Teclado"},
    {"codigo": "P002", "nombre": "Mouse"},
    {"codigo": "P003", "nombre": "Monitor"}
]

print("--- LISTA ORIGINAL ---")
print(productos)
print("-" * 35)

catalogo = {p["codigo"]: p["nombre"] for p in productos}

print("--- DICCIONARIO RESULTANTE ---")
print(catalogo)