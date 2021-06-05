import requests
import json

codEstaciones = {
    "28005002": ["5", "Alcalá de Henares"],
    "28006004": ["6", "Alcobendas"],
    "28007004": ["7", "Alcorcón"],
    "28102001": ["102", "Orusco de Tajuña"]
}

codMagnitudes = {
    "1": ["Dióxido de azufre", "ug/m3"],
    "6": ["Monóxido de carbono", "mg/m3"],
    "7": ["Monóxido de nitrógeno", "ug/m3"]
}

peticion = requests.get(
    "https://datos.comunidad.madrid/catalogo/dataset/cb5b856f-71a4-4e34-8539-84a7e994c972/resource/c9e3248b-9aac-4771-9935-749354ba0db2/download/calidad_aire_datos_dia.json")

contenido = json.loads(peticion.content)

listaEstaciones = contenido["data"]

localidadABuscar = "Orusco de Tajuña"

magnitudABUscar = "Monóxido de carbono"

for codigoDeEstacion in codEstaciones.keys():
    if codEstaciones[codigoDeEstacion][1] == localidadABuscar:
        print("Estacion encontrada")
        for codigoDeMagnitud in codMagnitudes.keys():
            if magnitudABUscar == codMagnitudes[codigoDeMagnitud][0]:
                print("Magnitud encontrada")
                print("Los ultmos resultados son: ")
                for estacion in listaEstaciones:
                    listaDatos = estacion["punto_muestreo"].split("_")
                    if codigoDeEstacion == listaDatos[0] and codigoDeMagnitud == listaDatos[1]:
                        for i in range(1, 25):
                            if i < 10:
                                valor = "h0"+str(i)
                            else:
                                valor = "h"+str(i)
                            if estacion[valor] != "":
                                print("La medicion de", magnitudABUscar, "a las", str(
                                    i)+":00 es de", estacion[valor], codMagnitudes[codigoDeMagnitud][1])
