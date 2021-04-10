import sys

num1= int(sys.argv[1])
num2= int(sys.argv[2])

if num1==num2:
    print("Los numeros son iguales")
elif num1>=num2:
    print(num1,"es mayor que",num2)
else:
    print(num2,"es mayor que",num1)
