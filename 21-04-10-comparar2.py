def comparar(num1,num2):
    if num1==num2:
        print("Los numeros son iguales")
    elif num1>=num2:
        print(num1,"es mayor que",num2)
    else:
        print(num2,"es mayor que",num1)

num1= int(input("Dime el primer numero: "))
num2= int(input("Dime el segundo numero: "))
print("_"*10)
comparar(num1,num2)