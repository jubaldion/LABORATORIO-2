total = 0
numero = int(input("Deposito (0 para terminar): "))

while numero != 0:
    total += numero
    print("Acumulado:", total)
    numero = int(input("Deposito (0 para terminar): "))

print("Total final:", total)