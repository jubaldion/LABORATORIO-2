# -------------------------------------------------------------
# ESTRUCTURA DEL GESTOR DE INVENTARIO
# - Lista de diccionarios para productos: almacena el inventario dinámico.
# - Tupla de categorías válidas: define opciones fijas e inmutables.
# - Ciclo del menú principal: controla la ejecución continua.
#   1. Registrar (valida código único, campos no vacíos, rangos y categoría).
#   2. Listar (muestra todos los registros o aviso si está vacío).
#   3. Buscar (localiza por código con bandera de control).
#   4. Actualizar (reemplaza stock validando no negativos).
#   5. Eliminar (remueve un diccionario de la lista si existe).
#   6. Filtrar sin stock (usa comprensión de listas).
#   7. Mostrar resumen (usa comprensiones y funciones agregadas).
# -------------------------------------------------------------

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")
productos = []
opcion = ""

while opcion != "0":
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        print("\n--- REGISTRAR PRODUCTO ---")
        codigo = input("Código: ").strip()
        
        codigo_repetido = False
        for p in productos:
            if p["codigo"] == codigo:
                codigo_repetido = True
                break
                
        if codigo_repetido or codigo == "":
            print("Error: El código no puede estar vacío ni repetido.")
        else:
            nombre = input("Nombre: ").strip()
            if nombre == "":
                print("Error: El nombre no puede estar vacío.")
            else:
                print(f"Categorías permitidas: {CATEGORIAS}")
                categoria = input("Categoría: ").strip()
                if categoria not in CATEGORIAS:
                    print("Error: Categoría no válida.")
                else:
                    precio = float(input("Precio: "))
                    if precio <= 0:
                        print("Error: El precio debe ser mayor a cero.")
                    else:
                        cantidad = int(input("Cantidad: "))
                        if cantidad < 0:
                            print(" Error: La cantidad no puede ser negativa.")
                        else:
                            # Crear diccionario y agregarlo a la lista
                            nuevo_producto = {
                                "codigo": codigo,
                                "nombre": nombre,
                                "categoria": categoria,
                                "precio": precio,
                                "cantidad": cantidad
                            }
                            productos.append(nuevo_producto)
                            print(" Producto registrado con éxito.")

    elif opcion == "2":
        print("\n--- LISTA DE PRODUCTOS ---")
        if len(productos) == 0:
            print("No hay registros en el inventario.")
        else:
            for p in productos:
                print(f"{p['codigo']} - {p['nombre']} - {p['categoria']} - ${p['precio']} - {p['cantidad']} unidades")

    elif opcion == "3":
        print("\n--- BUSCAR POR CÓDIGO ---")
        codigo_buscado = input("Ingrese el código a buscar: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break
                
        if encontrado is not None:
            print("\n¡Producto encontrado!")
            print(f"Código: {encontrado['codigo']}")
            print(f"Nombre: {encontrado['nombre']}")
            print(f"Categoría: {encontrado['categoria']}")
            print(f"Precio: ${encontrado['precio']}")
            print(f"Cantidad: {encontrado['cantidad']}")
        else:
            print(" No se encontró un producto con ese código.")

    elif opcion == "4":
        print("\n--- ACTUALIZAR EXISTENCIAS ---")
        codigo_buscado = input("Ingrese el código del producto a actualizar: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break
                
        if encontrado is not None:
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad para '{encontrado['nombre']}': "))
            if nueva_cantidad < 0:
                print(" Error: La cantidad no puede ser negativa. Se conservó el valor anterior.")
            else:
                encontrado["cantidad"] = nueva_cantidad
                print(" Existencias actualizadas con éxito.")
        else:
            print(" No se encontró un producto con ese código.")

    elif opcion == "5":
        print("\n--- ELIMINAR PRODUCTO ---")
        codigo_buscado = input("Ingrese el código del producto a eliminar: ").strip()
        encontrado_indice = None
        
        for i in range(len(productos)):
            if productos[i]["codigo"] == codigo_buscado:
                encontrado_indice = i
                break
                
        if encontrado_indice is not None:
            producto_eliminado = productos.pop(encontrado_indice)
            print(f"Producto '{producto_eliminado['nombre']}' eliminado correctamente.")
        else:
            print("El código ingresado no existe, por lo que no se realizó ninguna eliminación.")

    elif opcion == "6":
        print("\n--- PRODUCTOS SIN STOCK ---")
        
        agotados = [
            p["nombre"]
            for p in productos
            if p["cantidad"] == 0
        ]
        
        if len(agotados) == 0:
            print("No hay productos agotados.")
        else:
            print("Sin existencias:")
            for nombre in agotados:
                print(f"- {nombre}")

    elif opcion == "7":
        print("\n--- RESUMEN DEL INVENTARIO ---")
        if len(productos) == 0:
            print("El inventario está vacío.")
        else:
            total_productos = len(productos)
            total_unidades = sum([p["cantidad"] for p in productos])
            valor_inventario = sum([p["precio"] * p["cantidad"] for p in productos])
            
            categorias_utilizadas = {
                p["categoria"]
                for p in productos
            }
            
            print(f"Productos: {total_productos}")
            print(f"Unidades: {total_unidades}")
            print(f"Valor del inventario: ${valor_inventario:,.1f}")
            print(f"Categorías utilizadas: {', '.join(categorias_utilizadas)}")

    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print(" Opción no válida. Intente de nuevo.")