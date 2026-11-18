def buscar_paciente(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas):
    x = input("Ingrese el numero de historia: ")
    encontrado = False
    if x.isdigit():
        historia = int(x)
        for i in range(len(historias)):
            if historias[i] == historia:
                print("Paciente encontrado")
                print("N° HC:", str(historias[i]).zfill(6))
                print("Apellidos:", apellidos[i])
                print("Nombres", nombres[i])
                print("DNI:", dnis[i])
                print("Sexo", sexos[i])
                print("Nacimiento:", nacimientos[i])
                print("fecha de registro: ", fechas[i])
                encontrado = True
        if encontrado == False:
            print("Paciente no encontrado")