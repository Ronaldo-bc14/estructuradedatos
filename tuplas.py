cantidad = int(input("¿Cuántas ciudades deseas agregar? "))
ciudades_temp = []

if cantidad > 0:
    for i in range(cantidad):
        ciudad = input(f"Ingrese el nombre de la ciudad {i+1}: ")
        ciudades_temp.append(ciudad)
    ciudades = tuple(ciudades_temp)  # Convertimos lista a tupla
    print("Tupla de ciudades ingresadas:")
    print(ciudades)
else:
    print("La cantidad debe ser mayor a 0")
