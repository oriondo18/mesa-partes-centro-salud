def validar_dni(dni):
    if len(dni) == 8 and dni.isdigit():
        return True
    else:
        return False

dni = input("Ingrese el DNI: ")

if validar_dni(dni):
    print("DNI valido")
else:
    print("DNI invalido")