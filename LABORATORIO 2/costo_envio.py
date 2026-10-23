valor = float(input("Ingrese el valor de su compra"))
if valor >= 100000 and valor < 200000:
     print("El costo de envio es de $10.000")

elif valor > 200000:
     print("El costo del envio es GRATIS")

elif  valor < 100000:
     print("El costo del envio es de $18.000")     