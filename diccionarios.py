cantidad = int(input("¿Cuántas ciudades deseas agregar? "))
ciudades = {}

if cantidad > 0:
    for i in range(cantidad):
        ciudad = input(f"Ingrese el nombre de la ciudad {i+1}: ")
        ciudades[i+1] = ciudad
    print("Diccionario de ciudades ingresadas:")
    print(ciudades)
else:
    print("La cantidad debe ser mayor a 0")

