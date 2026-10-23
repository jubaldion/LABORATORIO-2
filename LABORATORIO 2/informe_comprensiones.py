ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

print("--- INFORME DE VENTAS Y COMPRENSIONES ---")
productos_altos_for = []
for v in ventas:
    if v["total"] > 100000:
        productos_altos_for.append(v["producto"])

print("1.A. Productos con ventas > $100.000 (Usando FOR):")
print(productos_altos_for)

productos_altos_comp = [v["producto"] for v in ventas if v["total"] > 100000]

print("1.B. Productos con ventas > $100.000 (Usando Comprensión):")
print(productos_altos_comp)

print("-" * 50)

categorias_diferentes = {v["categoria"] for v in ventas}
print("2. Categorías diferentes (Conjunto):")
print(categorias_diferentes)

print("-" * 50)

producto_valor = {v["producto"]: v["total"] for v in ventas}
print("3. Diccionario que relacione producto y valor de venta:")
print(producto_valor)

print("-" * 50)

suma_ventas = sum([v["total"] for v in ventas])
print("4. Suma de todas las ventas:")
print(f"${suma_ventas:,.0f}")