fichero = open("datos2.txt", "r", encoding="UTF-8")
listaLineas = fichero.readlines()
fichero.close()
print("Todas las Líneas: ")
print(listaLineas)
print("\n")

listaPalabras=[]
for linea in listaLineas:
    separado=linea.split(" ")
    listaPalabras+=separado

print("Todas las palabras: ")
print(listaPalabras)
print("\n")

listaLimpia=[]
for palabra in listaPalabras:
    limpiar=palabra.rstrip("\n").rstrip(",")
    listaLimpia.append(limpiar)

print("Plabras limpias: ")
print(listaLimpia)
print("\n")