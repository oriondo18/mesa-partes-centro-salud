def mostrar_pacientes(historias, apellidos, nombres, sexos, nacimientos, dnis):
    if len(historias) == 0:
        print("No hay pacientes registrados")
    else:
        print("Pacientes registrados:")
        for i in range(len(apellidos)):
            print("-", "N° HC", historias[i], apellidos[i], nombres[i], dnis[i], sexos[i], nacimientos[i])