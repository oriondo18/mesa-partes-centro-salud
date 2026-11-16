def validar_fecha(dia, mes, año):
    if dia.isdigit() == False or mes.isdigit() == False or año.isdigit() == False:
        return False

    dia = int(dia)
    mes = int(mes)
    año = int(año)

    if año < 1926 or año > 2026:
        return False
    if mes < 1 or mes > 12:
        return False
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        maximo = 30
    elif mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
            maximo = 29
        else:
            maximo = 28
    else:
        maximo = 31
    if dia >= 1 and dia <= maximo:
        return True
    else:
        return False