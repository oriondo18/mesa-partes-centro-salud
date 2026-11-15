def ordenar_pacientes(historias, apellidos, nombres, dnis):
    n = len(apellidos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if apellidos[j] > apellidos[j + 1]:
                aux = apellidos[j]
                apellidos[j] = apellidos[j + 1]
                apellidos[j + 1] = aux
                
                aux = historias[j]
                historias[j] = historias[j + 1]
                historias[j + 1] = aux

                aux = dnis[j]
                dnis[j] = dnis[j + 1]
                dnis[j + 1] = aux

                aux = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux