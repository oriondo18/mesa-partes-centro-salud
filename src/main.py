historias = []
apellidos = []
dnis = []

def validar_dni(dni):
    if len(dni) == 8 and dni.isdigit():
        return True
    else:
        return False

def registrar_paciente():
    apellido = input("Ingrese los apellidos: ")
    dni = input("Ingrese el DNI: ")
    if validar_dni(dni):
        historia = len(historias) + 1
        historias.append(historia)
        apellidos.append(apellido)
        dnis.append(dni)
        print("Paciente registrado con historia  N° HC", historia)
    else:
        print("DNI invalido, no se registro")

def buscar_paciente():
    texto = input("Ingrese el numero de historia: ")
    encontrado = False
    if texto.isdigit():
        historia = int(texto)
        for i in range(len(historias)):
            if historias[i] == historia:
                print("Paciente encontrado")
                print("Historia:", historias[i])
                print("Apellidos:", apellidos[i])
                print("DNI:", dnis[i])
                encontrado = True
        if encontrado == False:
            print("Paciente no encontrado")

registrar_paciente()
registrar_paciente()
buscar_paciente()
buscar_paciente()