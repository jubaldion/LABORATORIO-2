categorias = ("Electrónica", "Ropa", "Hogar", "Alimentos")

print("--- GESTIÓN DE CATEGORÍAS ---")

print("Categorías disponibles:")
for i, categoria in enumerate(categorias, 1):
    print(f"{i}. {categoria}")

categoria_usuario = input("\nIngrese una categoría para consultar: ").strip()

if categoria_usuario in categorias:
    print(f"¡Éxito! La categoría '{categoria_usuario}' SÍ pertenece a las opciones permitidas.")
else:
    print(f"Lo siento, la categoría '{categoria_usuario}' es desconocida o no está permitida.")
    
print(f"Cantidad total de categorías disponibles: {len(categorias)}")