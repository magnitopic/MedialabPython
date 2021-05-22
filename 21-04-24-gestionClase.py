def calcMedia():
    next

#Datos por defecto del fichero
clase = {
    "Gonzalo": {
        "notas": [5, 8, 9, 5, 4],
        "notaMedia": 6,
        "localidad": "Madrid"
    },
    "Victoria": {
        "notas": [8, 6, 9, 4, 8],
        "notaMedia": 7,
        "localidad": "Madrid"
    }
}


respuesta = input("Qué quieres hacer? (consultar/modificar/salir) ")

while (respuesta != "salir"):
    if respuesta == "consultar":
        deQuien = input("Qué alumno quieres consultar? ")
        if deQuien in clase.keys():
            queConsulto = input("Qué quieres consultar? ")
            if queConsulto in clase[deQuien].keys():
                print(clase[deQuien][queConsulto])
            else:
                print("No tengo esos datos.")
        else:
            print("No conozco a ese alumno")
    elif respuesta == "modificar":
        deQuien = input("Qué alumno quieres modificar? ")
        if deQuien in clase.keys():
            queCambio = input("Qué quieres modificar? ")
            if queCambio in clase[deQuien].keys():
                #Para diferenciar a notas de el resto de opciones cambio el texto del input
                if queCambio=="notas":
                    nuevoValor = input("Que valor quieres añadir? ")
                    nuevoValor=int(nuevoValor)
                    clase[deQuien][queCambio].append(nuevoValor)
                else:
                    nuevoValor = input("Por que valor lo cambias? ")
                    nuevoValor=int(nuevoValor)
                    clase[deQuien][queCambio]=nuevoValor
            else:
                print("No tengo esos datos.")
        else:
            print("No conozco a ese alumno")
    elif respuesta == "salir":
        print("Adiós!!")
        exit()
    else:
        print("Comando no reconocido")

    respuesta = input("Qué quieres hacer? (consultar/modificar/salir) ")

print("Adiós")