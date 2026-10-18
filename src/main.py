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
        numero = len(historias) + 1
        historia = str(numero).zfill(6)
        historias.append(historia)
        apellidos.append(apellido)
        dnis.append(dni)
        print("Paciente registrado con historia", historia)
    else:
        print("DNI invalido, no se registro")

registrar_paciente()
registrar_paciente()

print(historias)
print(apellidos)
print(dnis)