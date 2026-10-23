lista1 = ["Ana", "Carlos", "Sofía", "Carlos", "Pedro"]
lista2 = ["Sofía", "Lucía", "Ana", "Miguel", "Pedro"]

print("Listas originales con repetidos:")
print("Lista 1:", lista1)
print("Lista 2:", lista2)

personas_unicas = set(lista1 + lista2)

print("\n--- CONJUNTO DE PERSONAS ---")
print("Conjunto sin duplicados:", personas_unicas)

print(f"Cantidad total de personas diferentes: {len(personas_unicas)}")

personas_unicas.add("Valentina")
print("\nDespués de agregar a 'Valentina':", personas_unicas)

personas_unicas.discard("Carlos")
print("Después de eliminar a 'Carlos':", personas_unicas)