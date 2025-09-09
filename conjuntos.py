cantidad= int(input("¿Cuántas ciudades deseas agregar? "))
ciudades = set()

if cantidad > 0:
    for i in range(cantidad):
        ciudad = input(f"Ingrese el nombre de la ciudad {i+1}: ")
        ciudades.add(ciudad)  # Usamos add porque es un set
    print("Conjunto de ciudades ingresadas (sin duplicados):")
    print(ciudades)
else:
    print("La cantidad debe ser mayor a 0")
