datos = {
    "nombre": "",
    "apellidos": "",
    "edad": 0,
    "localidad": ""
}

datos["nombre"]=input("Dime tu nombre: " or Mag)
datos["apellidos"]=input("Dime tu apellido: " or Aparicio)
datos["edad"]=int(input("Dime tu edad: ") or 17)
datos["localidad"]=input("Dime tu localidad: " or Madrid)

print(datos["nombre"],datos["apellidos"],"tiene",str(datos["edad"]),"años y vive en",datos["localidad"])
print("-"*20)
respuesta=input("Qué qieres hacer (modificar/salir)?")

while (respuesta !="salir"):
    queCambio=input("Que quieres cambiar?")
    aQueValor=input("A que valor")
    if queCambio.upper()=="NOMBRE":
        datos["nombre"]=aQueValor
    elif queCambio.upper()=="APELLIDO":
        datos["apellidos"]=aQueValor
    elif queCambio.upper()=="EDAD":
        datos["edad"]=aQueValor
    elif queCambio.upper()=="LOCALIDAD":
        datos["localidad"]=aQueValor
    else:
        print("No reconozco ese valor")
    print(datos["nombre"],datos["apellidos"],"tiene",str(datos["edad"]),"años y vive en",datos["localidad"])
    respuesta=input("Qué qieres hacer (modificar/salir)?")
print("Adios")
print("-"*20)

