def validar_dni(dni):
    if len(dni) == 8 and dni.isdigit():
        return True
    else:
        return False