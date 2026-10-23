# 1. Crear la lista con seis calificaciones
calificaciones = [8.5, 6.0, 9.2, 7.5, 6.0, 10.0]

print("--- CALIFICACIONES ---")
print("Lista original:", calificaciones)
print("-" * 25)

# - Las tres primeras (usando slicing: desde el índice 0 hasta el 3 sin incluirlo)
print("Las tres primeras calificaciones:", calificaciones[:3])

# - Las dos últimas (usando slicing negativo: desde el penúltimo hasta el final)
print("Las dos últimas calificaciones:", calificaciones[-2:])

# - La cantidad total (usando len())
print("Cantidad total de calificaciones:", len(calificaciones))

# - Las notas ordenadas de menor a mayor, sin modificar el orden original (usando sorted())

print("Calificaciones ordenadas (de menor a mayor):", sorted(calificaciones))
print("Lista original intacta:", calificaciones) ()
nota_buscada = 6.0
cantidad_apariciones = calificaciones.count(nota_buscada)
print(f"La nota {nota_buscada} aparece {cantidad_apariciones} vez/veces.")