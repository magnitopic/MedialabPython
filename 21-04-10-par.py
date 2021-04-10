def par(num):
    if num%2==0:
        print("El numero",num,"es par.")
    else:
        print("El numero",num,"es impar.")

num = int(input("Dame el valor del numero: "))
print("_"*10)
par(num)