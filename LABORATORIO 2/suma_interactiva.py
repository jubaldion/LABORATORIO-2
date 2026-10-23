total = 0
depositos_validos = 0

numero = int(input("Depósito (0 para terminar): "))

while numero != 0:
    if numero < 0:
        print("El depósito no puede ser negativo.")
    else:
        total += numero
        depositos_validos += 1
        print("Ahorro acumulado:", total)
    
    numero = int(input("Depósito (0 para terminar): "))

print(f"Depósitos válidos: {depositos_validos}")
print(f"Total ahorro: {total}")