# Definimos dos conjuntos con aprendices inscritos (incluyendo nombres compartidos)
python_inscritos = {"Ana", "Carlos", "Sofía", "Pedro", "Lucía"}
java_inscritos = {"Sofía", "Pedro", "Miguel", "Valentina", "Carlos"}

print("--- INSCRIPCIONES A TALLERES ---")
print("Inscritos en Python:", python_inscritos)
print("Inscritos en Java:", java_inscritos)
print("")

al_menos_uno = python_inscritos | java_inscritos
print("1. Inscritos en al menos uno:", al_menos_uno)

ambos = python_inscritos & java_inscritos
print("2. Inscritos en ambos:", ambos)

solo_python = python_inscritos - java_inscritos
print("3. Inscritos únicamente en Python:", solo_python)

solo_java = java_inscritos - python_inscritos
print("4. Inscritos únicamente en Java:", solo_java)

uno_solo = python_inscritos ^ java_inscritos
print("5. Inscritos en uno solo de los talleres:", uno_solo)