#Operador and
esta_inscrito = True
tiene_documento = False

if esta_inscrito and tiene_documento:
    print("Puede ingresar.")
else:
    print("No cumple todos los requisitos.")

print("")
#Operador or
tiene_carnet = False
tiene_autorizacion = True

if tiene_carnet or tiene_autorizacion:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")

#operador not
bloqueado = False

if not bloqueado:
    print("La cuenta está habilitada.")
else:
    print("La cuenta está bloqueada.")