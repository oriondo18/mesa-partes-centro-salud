def ordenar_pacientes(historias, apellidos, nombres, sexos, nacimientos, dnis, fechas):
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

                aux = sexos[j]
                sexos[j] = sexos[j + 1]
                sexos[j + 1] = aux
                
                aux = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux

                aux = nacimientos[j]
                nacimientos[j] = nacimientos[j + 1]
                nacimientos[j + 1] = aux

                aux = fechas[j]
                fechas[j] = fechas[j + 1]
                fechas[j + 1] = aux