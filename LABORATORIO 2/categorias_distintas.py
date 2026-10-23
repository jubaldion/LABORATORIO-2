
productos = [
    {"nombre": "Teclado", "categoria": "Periféricos"},
    {"nombre": "Mouse", "categoria": "Periféricos"},
    {"nombre": "Disco", "categoria": "Componentes"}
]

print("--- PRODUCTOS ORIGINALES ---")
for p in productos:
    print(f"Producto: {p['nombre']} | Categoría: {p['categoria']}")

print("-" * 35)

categorias_diferentes = {producto["categoria"] for producto in productos}

print("--- CATEGORÍAS DISTINTAS (CONJUNTO) ---")
print(categorias_diferentes)
print(f"Total de categorías únicas: {len(categorias_diferentes)}")