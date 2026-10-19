historias = []
apellidos = []
dnis = []

def validar_dni(dni):
    if len(dni) == 8 and dni.isdigit():
        return True
    else:
        return False

def registrar_paciente():
    apellido = input("Ingrese los apellidos: ").upper()
    dni = input("Ingrese el DNI: ")
    if validar_dni(dni):
        historia = len(historias) + 1
        historias.append(historia)
        apellidos.append(apellido)
        dnis.append(dni)
        ordenar_pacientes()
        print("Paciente registrado con historia  N° HC", historia)
    else:
        print("DNI invalido, no se registro")

def buscar_paciente():
    x = input("Ingrese el numero de historia: ")
    encontrado = False
    if x.isdigit():
        historia = int(x)
        for i in range(len(historias)):
            if historias[i] == historia:
                print("Paciente encontrado")
                print("N° HC:", historias[i])
                print("Apellidos:", apellidos[i])
                print("DNI:", dnis[i])
                encontrado = True
        if encontrado == False:
            print("Paciente no encontrado")

def ordenar_pacientes():
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

def mostrar_pacientes():
    if len(historias) == 0:
        print("No hay pacientes registrados")
    else:
        print("Pacientes registrados:")
        for i in range(len(apellidos)):
            print("-", apellidos[i], dnis[i], "N° HC", historias[i])

while True:
    print("=== MESA DE PARTES - CENTRO DE SALUD ===")
    print("1. Registrar paciente")
    print("2. Buscar paciente")
    print("3. Mostrar pacientes")
    print("4. Salir")
    texto = input("Elija una opcion: ")
    if texto.isdigit():
        opcion = int(texto)
    else:
        opcion = 0
    match opcion:
        case 1:
            registrar_paciente()
        case 2:
            buscar_paciente()
        case 3:
            mostrar_pacientes()
        case 4:
            exit()
        case _:
            print("Opcion no valida")