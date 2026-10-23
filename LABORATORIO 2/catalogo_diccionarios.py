
productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 7},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

print("--- CATÁLOGO INICIAL ---")
for p in productos:
    print(p)

print("--- REGISTRAR NUEVO PRODUCTO ---")

nuevo_codigo = input("Ingrese el código del producto (ej: P004): ").strip()
nuevo_nombre = input("Ingrese el nombre del producto: ").strip()
nuevo_precio = float(input("Ingrese el precio: "))
nueva_cantidad = int(input("Ingrese la cantidad: "))

nuevo_producto = {
    "codigo": nuevo_codigo,
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
}

productos.append(nuevo_producto)

print("--- CATÁLOGO ACTUALIZADO ---")

for p in productos:
    print(f"Código: {p['codigo']} | Producto: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['cantidad']}")
