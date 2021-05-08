#lista=["car","bus","bike","plane","sakteboard"]

file=open("datos.txt","r",encoding="UTF-8")
lista=file.readlines()
file.close()

seguir=1

while seguir==1:
    palabraABuscar=input("Que palabra quieres buscar: ")
    encontrada=False
    contador=0

    if palabraABuscar=="salir()":
        seguir=0
        print("Adios!")
    else:
        for plabra in lista:
            if palabraABuscar==plabra.rstrip("\n"): #.rstrip() rlimina el character especificado
                print("Encontrada!")
                encontrada=True
                contador+=1

        if encontrada==False:
            print("No encontrada...")
        else:
            print("La palabra",palabraABuscar,"se repite",contador,"veces")
