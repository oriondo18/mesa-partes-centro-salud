def mostrar_pacientes(historias, apellidos, dnis):
    if len(historias) == 0:
        print("No hay pacientes registrados")
    else:
        print("Pacientes registrados:")
        for i in range(len(apellidos)):
            print("-", apellidos[i], dnis[i], "N° HC", historias[i])