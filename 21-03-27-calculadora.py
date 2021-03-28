def inicio():
    global num1,num2,op
    op = input("¿¿Que operación quires realizar??(sum/res/mul/div/sqrt/exit): ")
    if op == "exit":
        quit()
    elif op != "sum"and"res"and"mul"and"div"and"sqrt":
        print("Input no valido")
        inicio()
    num1 = input("Dime el primer numero: ")
    num2 = input("Dime el segundo numero: ")
    return op ,num1, num2

def suma(num1,num2):
    print("La suma de",str(num1),"y",str(num2),"es igual a:",str(int(num1)+int(num2)))

def res(num1,num2):
    print("La resta de",str(num1),"y",str(num2),"es igual a:",str(int(num1)-int(num2)))

def mul(num1,num2):
    print("La multiplicación de",str(num1),"y",str(num2),"es igual al:",str(int(num1)*int(num2)))

def div(num1,num2):
    print("La división de",str(num1),"y",str(num2),"es igual al:",str(int(num1)/int(num2)))

def sqrt(num1,num2):
    print(str(num1),"elevado a",str(num2),"nos da como resultado:",str(int(num1)+int(num2)))

inicio()
if op == "sum":
    suma(num1,num2)
    inicio()
elif op == "res":
    res(num1,num2)
    inicio()
elif op == "mul":
    mul(num1,num2)
    inicio()
elif op == "div":
    div(num1,num2)
    inicio()
elif op == "sqrt":
    sqrt(num1,num2)
    inicio()
