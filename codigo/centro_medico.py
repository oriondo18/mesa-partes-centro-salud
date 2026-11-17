from registro.registrar_paciente import registrar_paciente
from busqueda.buscar_paciente import buscar_paciente
from presentacion.mostrar_pacientes import mostrar_pacientes
from autenticacion.iniciar_sesion import iniciar_sesion
from archivos.guardar_datos import guardar_datos
from archivos.cargar_datos import cargar_datos

historias = []
apellidos = []
nombres = []
dnis = []
sexos = []
nacimientos= []
fechas = []

usuarios = ["RAMIREZ", "MARTINEZ"]
claves = ["r123", "m123"]

iniciar_sesion(usuarios, claves)
cargar_datos(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas)

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
            registrar_paciente(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas)
            guardar_datos(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas)
        case 2:
            buscar_paciente(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas)
        case 3:
            mostrar_pacientes(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas)
        case 4:
            exit()
        case _:
            print("Opcion no valida")

