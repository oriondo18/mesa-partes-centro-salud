def cargar_usuarios(usuarios, claves, roles):
    archivo = open("datos/usuarios.csv", "r", encoding="utf-8")

    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            datos = linea.split(";")
            usuarios.append(datos[0])
            claves.append(datos[1])
            roles.append(datos[2])

    archivo.close()