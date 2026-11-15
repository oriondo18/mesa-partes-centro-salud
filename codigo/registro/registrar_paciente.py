from validaciones.validar_dni import validar_dni
from ordenamiento.ordenar_pacientes import ordenar_pacientes

def registrar_paciente(historias, apellidos, nombres, dnis):
    apellido = input("Ingrese apellidos: ").upper()
    nombre = input("ingrese nombres: ").upper()
    dni = input("Ingrese el DNI: ")
    if validar_dni(dni):
        repetido = False
        for i in range(len(dnis)):
            if dnis[i] == dni:
                repetido = True
        if repetido == True:
            print("Este DNI ya esta registrado, no se registró")
        else:
            historia = len(historias) + 1
            historias.append(historia)
            apellidos.append(apellido)
            dnis.append(dni)
            nombres.append(nombre)
            ordenar_pacientes(historias, apellidos, nombres, dnis)
            print("Paciente registrado con historia  N° HC", historia)
    else:
        print("DNI invalido, no se registró")