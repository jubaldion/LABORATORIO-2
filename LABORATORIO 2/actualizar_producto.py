producto = {
    "codigo": 338, 
    "nombre": "mouse",
    "precio": 60000.0,
    "cantidad": 10,  
    
}

print("--- DICCIONARIO INICIAL ---")
print(producto)

print("\nNombre del producto:", producto["nombre"])

precio = float(input("Ingrese el precio del producto: "))
if precio > 0:
    print("Precio válido:", producto["precio"])
    producto["precio"] = precio
    print("Precio actualizado:", producto["precio"])

else:
    print("Error: El precio debe ser mayor a cero. No se actualizó.")

for clave, valor in producto.items():
    print(f"- {clave}: {valor}")    

