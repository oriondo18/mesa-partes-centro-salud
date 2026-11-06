from registro.registrar_paciente import registrar_paciente
from busqueda.buscar_paciente import buscar_paciente
from presentacion.mostrar_pacientes import mostrar_pacientes

historias = []
apellidos = []
dnis = []

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
            registrar_paciente(historias, apellidos, dnis)
        case 2:
            buscar_paciente(historias, apellidos, dnis)
        case 3:
            mostrar_pacientes(historias, apellidos, dnis)
        case 4:
            exit()
        case _:
            print("Opcion no valida")
