numeros = [3, 8, 12, 5, 20, 7]

mayores = [numero for numero in numeros if numero >= 10]

print(mayores)

print("--" * 30)
notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]

aprobadas = [nota for nota in notas if nota >= 3.0]
print("Notas aprobadas:", aprobadas)


aprobadas = [nota for nota in notas if nota <= 3.0]
print("Notas reprobadas:", aprobadas)

aprobadas = [nota * 2 for nota in notas]
print("Notas multiplicadas por 2:", aprobadas)




