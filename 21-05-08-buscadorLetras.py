# lista=["car","bus","bike","plane","sakteboard"]

file = open("datos2.txt", "r", encoding="UTF-8")
lista = file.readlines()
file.close()

seguir = 1

while seguir == 1:
    letraABuscar = input("Que letra quieres buscar: ")
    encontrada = False
    contador = 0

    if letraABuscar == "salir()":
        seguir = 0
        print("Adios!")
    else:
        for plabra in lista:
            for letra in plabra.rstrip("\n"):
                if letra == letraABuscar:  # .rstrip() rlimina el character especificado
                    print("Encontrada!")
                    encontrada = True
                    contador += 1

        if encontrada == False:
            print("No encontrada...")
        else:
            print("La letra", letraABuscar, "se repite", contador,"veces")
