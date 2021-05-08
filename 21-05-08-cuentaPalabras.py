import sys
fichero = open(sys.argv[1], "r", encoding="UTF-8")  #Se le tiene que pasar como argumento el archivo(datos.txt / datos2.txt / el_quijote.txt)
listaLineas = fichero.readlines()
fichero.close()

listaPalabras=[]
for linea in listaLineas:
    separado=linea.split(" ")
    listaPalabras+=separado

listaLimpia=[]
for palabra in listaPalabras:
    limpiar=palabra.rstrip("\n").rstrip(",").rstrip(".").rstrip("!")
    listaLimpia.append(limpiar)

seguir=1

while seguir==1:
    palabraABuscar=input("Que palabra quieres buscar: ")
    encontrada=False
    contador=0

    if palabraABuscar=="salir()":
        seguir=0
        print("Adios!")
    else:
        for plabra in listaLimpia:
            if palabraABuscar==plabra: #.rstrip() rlimina el character especificado
                encontrada=True
                contador+=1

        if encontrada==False:
            print("No encontrada...")
        else:
            print("La palabra",palabraABuscar,"se repite",contador,"veces")