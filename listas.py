cantidad=0
i=0
ciudades=[]

cantidad=int(input("ingresa la cant. de ciudades que deseas agregar"))

if cantidad>0:
    while i<cantidad:
        ciudad=input("ingresa el nombre de la ciudad: ")
        ciudades.append(ciudad)
        i+=1
    print("Las ciudades ingresadas son:")
    for ciudad in ciudades:
        print(ciudad)
else:
    print("la cantidad debe ser mayor a 0")
