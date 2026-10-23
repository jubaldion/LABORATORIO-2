
coord_1 = (4.6097, -74.0817)
coord_2 = (6.2442, -75.5812)
coord_3 = (3.4516, -76.5320)

print("--- COORDENADAS ---")

lat_bogota, lon_bogota = coord_1
lat_medellin, lon_medellin = coord_2
lat_cali, lon_cali = coord_3

print(f"Bogotá -> Latitud: {lat_bogota}, Longitud: {lon_bogota}")
print(f"Medellín -> Latitud: {lat_medellin}, Longitud: {lon_medellin}")
print(f"Cali -> Latitud: {lat_cali}, Longitud: {lon_cali}")

sede_principal = ("SED-001", "Sede Norte", "Bogotá")

print("--- INFORMACIÓN DE LA SEDE ---")
codigo, nombre, ciudad = sede_principal

print(f"Código de la sede: {codigo}")
print(f"Nombre: {nombre}")
print(f"Ciudad: {ciudad}")