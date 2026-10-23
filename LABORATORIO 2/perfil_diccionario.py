perfil = {
    "ficha": 3388087,  
    "nombre": "Juliana",
    "trimestre": 5,
    "promedio": 10.0,  
    "activo": True     
}

print("--- DICCIONARIO INICIAL ---")
print(perfil)

print("Nombre del aprendiz:", perfil["nombre"])

perfil["trimestre"] = 6
print("Trimestre actualizado:", perfil["trimestre"])

perfil["correo"] = "juliana@sena.edu.co"
print("Correo agregado:", perfil["correo"])

print("--- DICCIONARIO FINAL ---")
print(perfil)