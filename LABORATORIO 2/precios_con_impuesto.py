precios = [10000, 20000, 50000, 80000]

print("--- PRECIOS ORIGINALES ---")
print(precios)
print("-" * 30)

precios_con_iva_for = []

for precio in precios:
    precio_con_impuesto = precio * 1.19
    precios_con_iva_for.append(precio_con_impuesto)

print("1. Con bucle for y append():")
print(precios_con_iva_for)

print("-" * 30)

precios_con_iva_comprension = [precio * 1.19 for precio in precios]

print("2. Con comprensión de listas:")
print(precios_con_iva_comprension)

print("-" * 30)

if precios_con_iva_for == precios_con_iva_comprension:
    print("¡Comprobación exitosa! Ambos métodos dan exactamente el mismo resultado.")
else:
    print("Los resultados son diferentes.")