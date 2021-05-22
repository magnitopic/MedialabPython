import sys

nombreOrigen = sys.argv[1]

ficheroOrigen = open(nombreOrigen, "r", encoding="utf-8")

listaLineas = ficheroOrigen.readlines()

ficheroOrigen.close()

listaNumeros = []

for linea in listaLineas:
    listaNumeros += linea.split(" ")

listaFinal = []

for elemento in listaNumeros:
    listaFinal.append(elemento.rstrip("\n"))

contadorNumero = len(listaFinal)

sumaTotal = 0
print(listaFinal)
for numero in listaFinal:
    sumaTotal += int(numero)

multiplicacionTotal = 1

for numero in listaFinal:
    multiplicacionTotal *= int(numero)

textoSalida = "Se han detectado " + str(contadorNumero) + " números.\n" + "La suma de todos ellos es " + str(
    sumaTotal) + ".\n" + "La multiplicación de todos ellos es " + str(multiplicacionTotal) + "."

ficheroSalida = open("numerosAnalizados.txt", "w", encoding="utf-8")
ficheroSalida.write(textoSalida)
ficheroSalida.close()
print("Programa terminado.")
