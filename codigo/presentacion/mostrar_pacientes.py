def mostrar_pacientes(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas):
    if len(historias) == 0:
        print("No hay pacientes registrados")
    else:
        print("Pacientes registrados:")
        for i in range(len(apellidos)):
            print("-", "N° HC", str(historias[i]).zfill(6), apellidos[i], nombres[i], "| DNI:", dnis[i], "| Nac:", nacimientos[i], "| Sexo:", sexos[i], "| Registro:", fechas[i])