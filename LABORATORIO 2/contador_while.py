contador = 0
numero = int(input("Ingrese un numero: "))

while numero != 0:
    print(numero)
    contador += 1 
    numero = int(input("Ingrese un numero: "))

print(f"El numero ingresado es cero, el programa ha finalizado. Se ingresaron {contador} números diferentes de cero.")