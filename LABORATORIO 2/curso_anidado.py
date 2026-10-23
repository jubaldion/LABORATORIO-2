curso = {
    "nombre": "Fundamentos de Python",
    "codigo": 1,  
    "temas": ["Variables y tipos", "Estructuras de control", "Funciones"],  
    "instructor": {
        "nombre": "María",
        "area": "Software"
    }
}  

print("Curso:", curso["nombre"])

print("Segundo tema:", curso["temas"][1])

print("Instructor:", curso["instructor"]["nombre"])

print("Cantidad de temas:", len(curso["temas"]))