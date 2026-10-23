contador = 0
numero = int(input("Ingrese un numero:"))

while numero != 0:
    print(numero)
    contador += 1
    numero = int(input("Ingrese un numero:" ))

if numero == 0:
    print("El numero ingresado es cero, el programa ha finalizado.")
    
    print(f"Se ingresaron {contador} numeros antes de ingresar cero.")