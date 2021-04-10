import sys

def suma(num1,num2):
    print("La suma entre",num1,"y",num2,"es igual a:",num1+num2)

def resta(num1,num2):
    print("La resta entre",num1,"y",num2,"es igual a:",num1-num2)

def par(num):
    if num%2==0:
        print("El numero",num,"es par.")
    else:
        print("El numero",num,"es impar.")

def mayor(num1,num2):
    if num1==num2:
        print("Los numeros son iguales")
    elif num1>=num2:
        print(num1,"es mayor que",num2)
    else:
        print(num2,"es mayor que",num1)

response= sys.argv[1]
if response=="par":
    num = int(input("Dame el valor del numero: "))
    par(num)
else:
    num1= int(input("Dime el primer numero: "))
    num2= int(input("Dime el segundo numero: "))
    if response=="suma":
        suma(num1,num2)
    if response=="resta":
        resta(num1,num2)
    if response=="mayor":
        mayor(num1,num2)