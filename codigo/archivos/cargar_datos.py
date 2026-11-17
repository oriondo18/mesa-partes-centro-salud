def cargar_datos(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas):
    archivo = open("datos/pacientes.csv", "r", encoding="utf-8")

    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            datos = linea.split(";")
            historias.append(int(datos[0]))
            apellidos.append(datos[1])
            nombres.append(datos[2])
            dnis.append(datos[3])
            sexos.append(datos[4])
            nacimientos.append(datos[5])
            fechas.append(datos[6])

    archivo.close()