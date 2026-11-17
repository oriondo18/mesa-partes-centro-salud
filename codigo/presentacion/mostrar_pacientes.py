def mostrar_pacientes(historias, apellidos, nombres, sexos, nacimientos, dnis, fechas):
    if len(historias) == 0:
        print("No hay pacientes registrados")
    else:
        print("Pacientes registrados:")
        for i in range(len(apellidos)):
            print("-", "N° HC", historias[i], apellidos[i], nombres[i], "| DNI:", dnis[i], "| Nac:", nacimientos[i], "| Sexo:", sexos[i], "| Registro:", fechas[i])