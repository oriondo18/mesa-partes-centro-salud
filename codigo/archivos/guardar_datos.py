def guardar_datos(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas):
    archivo = open("datos/pacientes.csv", "w", encoding="utf-8")

    for i in range(len(historias)):
        linea = str(historias[i]) + ";" + apellidos[i] + ";" + nombres[i] + ";" + dnis[i] + ";" + sexos[i] + ";" + nacimientos[i] + ";" + fechas[i] + "\n"
        archivo.write(linea)

    archivo.close()