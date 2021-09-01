'''
Desfibriladores de la Comunidad de Madrid
https://datos.comunidad.madrid/catalogo/dataset/desfibriladores_externos_fuera_ambito_sanitario

Coordenadas geodésicas de Calle Cenicero, 11, cerca de la plaza de Atocha (Madrid), coordenadas geodésicas:
40.41031389475527, -3.693225664534518

Convertimos las coordenadas geodésicas en coordenadas UTM con la página del Instituto Geográfico Nacional. https://www.ign.es/web/ign/portal/calculadora-geodesica

Coordenadas UTM:
DATOS ETRS89

X UTM: 441181.932
Y UTM: 4473530.336
'''

import requests
import json

# Preguntar datos al usuario
print("\nTe voy a pedir tus coordenadas X Y para determinar donde se localiz el desfibrilador mas cercano a tí.")
Ux = float(input("Dime tu coordenada X: ") or 441181.932)
Uy = float(input("Dime tu coordenada Y: ") or 4473530.336)

# Se recogen datos de la API de la comunidad de Madrid: https://datos.comunidad.madrid/catalogo/dataset/desfibriladores_externos_fuera_ambito_sanitario/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed
peticion = requests.get(
    "https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json")
contenido = json.loads(peticion.content)
datos = contenido["data"]

# recorremos todos los elementos de datos y calculamos la distancia de cada desfibrilador a nosotros
result = []
for i in range(len(datos)):
    x = Ux-float(datos[i]["direccion_coordenada_x"])
    y = Uy-float(datos[i]["direccion_coordenada_y"])
    result.append((x**2+y**2)**.5)

# Recogemos la posición del punto más cercano
for j in range(len(result)):
    if (result[j] == min(result, key=abs)):
        posicion = j

# Se imprime el resultado
print("\nEl desfibrilador más cercano a tí se encuentra en",
      datos[posicion]["direccion_via_codigo"], datos[posicion]["direccion_via_nombre"], "en", datos[posicion]["municipio_nombre"])
print(datos[posicion]["direccion_ubicacion"])
