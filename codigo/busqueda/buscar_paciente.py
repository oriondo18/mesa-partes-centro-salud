def buscar_paciente(historias, apellidos, nombres, sexos, dnis):
    x = input("Ingrese el numero de historia: ")
    encontrado = False
    if x.isdigit():
        historia = int(x)
        for i in range(len(historias)):
            if historias[i] == historia:
                print("Paciente encontrado")
                print("N° HC:", historias[i])
                print("Apellidos:", apellidos[i])
                print("Nombres", nombres[i])
                print("DNI:", dnis[i])
                encontrado = True
        if encontrado == False:
            print("Paciente no encontrado")