entrada = input("Dame un numero: ")
resultado=0

while (True):
    if entrada == "exit()":
        confirmacion=input("¿Seguro? (S/N): ")
        if confirmacion.upper()== "S":
            break
    elif entrada.isnumeric():
        resultado += int(entrada)
        print(resultado)
    entrada=input("Dame un numero: ")

print("Programa terminado.")