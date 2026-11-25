from autenticacion.codificar_clave import codificar_clave

def iniciar_sesion(usuarios, claves, roles):
    intentos = 0
    acceso = False
    rol = ""

    while acceso == False:
        print("========================")
        usuario = input("Ingrese su usuario: ").strip().upper()
        clave = input("Ingrese su clave: ")
        clave_codificada = codificar_clave(clave)

        for i in range(len(usuarios)):
            if usuarios[i] == usuario and claves[i] == clave_codificada:
                acceso = True
                rol = roles[i]

        if acceso == True:
            print("Acceso permitido, rol:", rol)
        else:
            intentos = intentos + 1
            print("Usuario o clave incorrectos")
            print("Te quedan", 3 - intentos, "intento(s)")
            if intentos == 3:
                print("Acceso denegado")
                exit()

    return rol