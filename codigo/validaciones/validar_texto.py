def validar_texto(texto):
    if len(texto) >= 2 and texto.replace(" ", "").isalpha():
        return True
    else:
        return False