words=["car", "boat", "bike", "lorry"]
respuesta="S"

while ((respuesta.upper()=="S") and (len(words)>0)):
    print("La lista actualemte tiene estos valores: ")
    for i in words:
        print(i)
    print("-"*10)
    respuesta=input("Quieres eliminar el ultimo valor? S/N: ")
    if respuesta.upper()=="S":
        eliminado=words.pop()
        print(eliminado)

print("Adios")