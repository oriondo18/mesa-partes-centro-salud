from datetime import date
from validaciones.validar_dni import validar_dni
from validaciones.validar_sexo import validar_sexo
from validaciones.validar_fecha import validar_fecha
from validaciones.validar_texto import validar_texto
from ordenamiento.ordenar_pacientes import ordenar_pacientes

def registrar_paciente(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas):
    apellido = input("Ingrese apellidos: ").strip().upper()
    while validar_texto(apellido) == False:
        print("Apellidos invalidos, use solo letras")
        apellido = input("Ingrese los apellidos: ").strip().upper()

    nombre = input("Ingrese los nombres: ").strip().upper()
    while validar_texto(nombre) == False:
        print("Nombres invalidos, use solo letras")
        nombre = input("Ingrese los nombres: ").strip().upper()

    sexo = input("Ingrese sexo (M/F): ").upper()
    while validar_sexo(sexo) == False:
        print("Sexo invalido, escriba M o F")
        sexo = input("Ingrese sexo (M/F): ").upper()

    print("Fecha de nacimiento")
    dia = input("Dia: ")
    mes = input("Mes: ")
    año = input("Año: ")
    while validar_fecha(dia, mes, año) == False:
        print("Fecha invalida, ingrese de nuevo")
        dia = input("Dia: ")
        mes = input("Mes: ")
        año = input("Año: ")
    nacimiento = dia.zfill(2) + "/" + mes.zfill(2) + "/" + año
    
    dni = input("Ingrese el DNI: ")
    repetido = False
    for i in range(len(dnis)):
        if dnis[i] == dni:
            repetido = True

    if validar_dni(dni) == False:
        print("DNI invalido, no se registró")
    elif repetido == True:
        print("Este DNI ya esta registrado, no se registró")
    else:
        historia = len(historias) + 1
        fecha_registro = date.today().strftime("%d/%m/%Y")

        historias.append(historia)
        apellidos.append(apellido)
        nombres.append(nombre)
        dnis.append(dni)
        sexos.append(sexo)
        nacimientos.append(nacimiento)
        fechas.append(fecha_registro)
        ordenar_pacientes(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas)
        print("Paciente registrado con historia N° HC", str(historia).zfill(6))