file=input("Dime un fichero o exit() para salir: ")

while file != "exit()":
    fichero=open(file,"r",encoding="utf-8")
    listaLineas=fichero.readlines()
    fichero.close()
    
    listaPalabras=[]
    for linea in listaLineas:
        listaPalabras+=linea.split(" ")

    contador=len(listaPalabras)

    analisisSalida="El fichero "+ file+" contiene "+str(contador)+" palabras.\n"
    print(analisisSalida)
    fichero = open("resultado.txt", "a", encoding="utf-8")
    fichero.write(str(analisisSalida))
    fichero.close()

    file=input("Dime un fichero(o exit() para salir): ")
