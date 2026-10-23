respuesta = input("¿Tiene autorización? : ").strip().lower()
tiene_autorizacion = respuesta == "si"
docs = int (input("Cantidad de docs entregados"))

edad = int(input("Edad: "))

if edad >= 16 and tiene_autorizacion and docs:
    print("Puede ingresar.")

elif edad < 16:
   print ("Solicitud rechazada")
elif docs < 3 :
   print ("Solicitud rechazada")
elif tiene_autorizacion:
   print ("Solicitud rechazada")
  


