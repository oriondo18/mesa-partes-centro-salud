from validaciones.validar_dni import validar_dni
from validaciones.validar_sexo import validar_sexo
from ordenamiento.ordenar_pacientes import ordenar_pacientes

def registrar_paciente(historias, apellidos, nombres, sexos, dnis):
    apellido = input("Ingrese apellidos: ").upper()
    nombre = input("Ingrese nombres: ").upper()
    sexo = input("Ingrese sexo (M/F): ").upper()
    while validar_sexo(sexo) == False:
        print("Sexo invalido, escriba M o F")
        sexo = input("Ingrese sexo (M/F): ").upper()
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
            nombres.append(nombre)
            sexos.append(sexo)
            dnis.append(dni)
            ordenar_pacientes(historias, apellidos, nombres, sexos, dnis)
            print("Paciente registrado con historia  N° HC", historia)
    else:
        print("DNI invalido, no se registró")