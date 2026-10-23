productos = ["Teclado", "Mouse"]
nuevo_producto = input("Ingrese un nuevo producto: ").strip()

if nuevo_producto == "":
    print("Error: El producto no puede estar vacío.")

elif nuevo_producto in productos:
    print("El producto ya está repetido en la lista.")

else:
    productos.append(nuevo_producto)
    print("Producto agregado con éxito.")

print("Lista final de productos:", productos)