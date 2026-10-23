notas_total = int(input("Cuantas notas va a registrar"))

if notas_total <= 0:
    print("El numero de notas debe ser mayor a cero")

else: 
    suma_notas = 0
    for i in range(notas_total):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        suma_notas += nota

    promedio = suma_notas / notas_total
    print(f"El promedio de las notas es: {promedio}")