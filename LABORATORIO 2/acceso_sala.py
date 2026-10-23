respuesta = input("¿Tiene autorización? : ").strip().lower()
tiene_autorizacion = respuesta == "si"

edad = int(input("Edad: "))

if edad >= 18 :
    print("Puede ingresar.")
elif edad < 18 and tiene_autorizacion:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")