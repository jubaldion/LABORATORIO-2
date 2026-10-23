codigos = [" p001 ", "P002", "", " p003", "  "]

codigos_normalizados = [codigo.strip().upper() for codigo in codigos if codigo.strip() != ""]

print("--- LISTA NORMALIZADA ---")
print(codigos_normalizados)