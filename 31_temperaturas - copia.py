temperaturas="12.4,23.6,17.8,3.5,29.0,11.6"
#¿Cual es la temperatura más baja?
print("La temperatura más baja es: ",min([float(t) for t in temperaturas.split(",")]))