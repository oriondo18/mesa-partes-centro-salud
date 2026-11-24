from registro.registrar_paciente import registrar_paciente
from busqueda.buscar_paciente import buscar_paciente
from presentacion.mostrar_pacientes import mostrar_pacientes
from autenticacion.iniciar_sesion import iniciar_sesion
from autenticacion.registrar_usuario import registrar_usuario
from archivos.guardar_datos import guardar_datos
from archivos.cargar_datos import cargar_datos
from archivos.cargar_usuarios import cargar_usuarios

historias = []
apellidos = []
nombres = []
dnis = []
sexos = []
nacimientos= []
fechas = []

usuarios = []
claves = []
roles = []

cargar_usuarios(usuarios, claves, roles)
while len(usuarios) == 0:
    print("No hay usuarios registrados. Cree el administrador inicial")
    registrar_usuario(usuarios, claves, roles, "ADMIN")

rol = iniciar_sesion(usuarios, claves, roles)
cargar_datos(historias, apellidos, nombres, dnis, sexos, nacimientos, fechas)

while True:
    print("=== MESA DE PARTES - CENTRO DE SALUD ===")
    print("1. Registrar paciente")
    print("2. Buscar paciente")
    print("3. Mostrar pacientes")
    print("4. Salir")
    if rol == "ADMIN":
        print("5. Registrar usuario")
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
        case 5:
            if rol == "ADMIN":
                registrar_usuario(usuarios, claves, roles, "ADMISION")
            else:
                print("No tiene permiso para esta opcion")
        case _:
            print("Opcion no valida")
