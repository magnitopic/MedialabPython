import requests
import json

print("\nTe voy a pedir tus coordenadas X Y para determinar donde se localiz el desfibrilador mas cercano a tí.")
Ux=float(input("Dime tu coordenada X: ") or 442408)
Uy=float(input("Dime tu coordenada Y: ") or 4479871)



peticion = requests.get("https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json")

contenido = json.loads(peticion.content)
datos=contenido["data"]

result=[]
for i in range(len(datos)):
    x=(Ux-float(datos[i]["direccion_coordenada_x"]))
    y=(Uy-float(datos[i]["direccion_coordenada_y"]))
    result.append((x+y)/2)
print(result)


for j in range(len(result)):
    if (result[j] == min(result, key=abs)):
        posicion=j
print(posicion)

print("\nEl desfibrilador más cercano a tí se encuentra en",datos[posicion]["direccion_via_codigo"],datos[posicion]["direccion_via_nombre"],",",datos[posicion]["municipio_nombre"])


#40.53891951292085, -3.8598928612811054