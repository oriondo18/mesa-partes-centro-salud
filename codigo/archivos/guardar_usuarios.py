def guardar_usuarios(usuarios, claves, roles):
    archivo = open("datos/usuarios.csv", "w", encoding="utf-8")

    for i in range(len(usuarios)):
        linea = usuarios[i] + ";" + claves[i] + ";" + roles[i] + "\n"
        archivo.write(linea)

    archivo.close()