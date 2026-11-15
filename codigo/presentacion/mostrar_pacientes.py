def mostrar_pacientes(historias, apellidos, nombres, dnis):
    if len(historias) == 0:
        print("No hay pacientes registrados")
    else:
        print("Pacientes registrados:")
        for i in range(len(apellidos)):
            print("-", apellidos[i], nombres[i], dnis[i], "N° HC", historias[i])