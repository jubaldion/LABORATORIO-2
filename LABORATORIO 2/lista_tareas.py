tareas = []
opcion = ""

while opcion != "0":
    print("--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Consultar cantidad")
    print("0. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        nueva_tarea = input("Ingrese la nueva tarea: ").strip()
        if nueva_tarea == "":
            print("Error: La tarea no puede estar vacía.")
        else:
            tareas.append(nueva_tarea)
            print("Tarea agregada")
            
    elif opcion == "2":
        if len(tareas) == 0:
            print("La lista de tareas está vacía.")
        else:
            print("Lista de tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
                
    elif opcion == "3":
        cantidad = len(tareas)
        print(f"Cantidad actual de tareas: {cantidad}")
        
    elif opcion == "0":
        print("Saliendo del programa")
        
    else:
        print("Opción no válida. Por favor, seleccione un número del menú.")