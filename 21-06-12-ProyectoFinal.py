import requests
import json

# Preguntar datos al usuario
print("\nTe voy a pedir tus coordenadas X Y para determinar donde se localiz el desfibrilador mas cercano a tí.")
Ux = float(input("Dime tu coordenada X: ") or 442408)
Uy = float(input("Dime tu coordenada Y: ") or 4479871)

# Se recogen datos de la API de la comunidad de Madrid: https://datos.comunidad.madrid/catalogo/dataset/desfibriladores_externos_fuera_ambito_sanitario/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed
peticion = requests.get(
    "https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json")
contenido = json.loads(peticion.content)
datos = contenido["data"]

# recorremos todos los elementos de datos y calculamos la distancia de cada desfibrilador a nosotros
result = []
for i in range(len(datos)):
    x = (Ux-float(datos[i]["direccion_coordenada_x"]))
    y = (Uy-float(datos[i]["direccion_coordenada_y"]))
    result.append((x+y)/2)
print(result)

# Recogemos la posición del punto más cercano
for j in range(len(result)):
    if (result[j] == min(result, key=abs)):
        posicion = j
print(posicion)

# Se imprime el resultado
print("\nEl desfibrilador más cercano a tí se encuentra en",
      datos[posicion]["direccion_via_codigo"], datos[posicion]["direccion_via_nombre"], ",", datos[posicion]["municipio_nombre"])
