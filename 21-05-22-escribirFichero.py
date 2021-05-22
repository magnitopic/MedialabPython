# La opción W usa el fichero indicado y si no existe lo crea
# El archivo tetxt.txt ha sido creado desde este programa
'''fichero = open("test.txt", "w", encoding="utf-8")

fichero.write("Hola Mundo")

fichero.close()'''


palabra = ""
resultado = ""

while palabra != "salir()":
    palabra = input("Dame una palabra: ")
    if palabra != "imprimir()" and palabra != "salir()":
        resultado += palabra+" "
    elif palabra == "imprimir()":
        #Si se usa A en lugar de W el texto se añade al fichero en lugar de remplazarlo
        fichero = open("test.txt", "w", encoding="utf-8")
        fichero.write(resultado)
        fichero.close()
        print("Fichero creado")
    else:
        print("Fin de programa.")
        print("Adiós!")
