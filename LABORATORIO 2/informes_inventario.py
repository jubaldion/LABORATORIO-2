
productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

print("--- INFORMES DE INVENTARIO ---")

sin_existencias = [
    p["nombre"] 
    for p in productos 
    if p["cantidad"] == 0
]
print("1. Productos sin existencias:", sin_existencias)

precio_alto = [
    p["nombre"] 
    for p in productos 
    if p["precio"] > 100000
]
print("2. Productos con precio > $100.000:", precio_alto)

cantidades_diferentes = {
    p["cantidad"] 
    for p in productos
}
print("3. Cantidades diferentes (Conjunto):", cantidades_diferentes)

nombre_y_precio = {
    p["nombre"]: p["precio"] 
    for p in productos
}
print("4. Diccionario de nombre y precio:", nombre_y_precio)