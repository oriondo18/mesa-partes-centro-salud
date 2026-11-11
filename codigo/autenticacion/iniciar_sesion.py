def iniciar_sesion(usuarios, claves):
    intentos = 0
    acceso = False

    while acceso == False:
        print("===INICIAR SESION===")
        usuario = input("Ingrese su usuario: ").upper()
        clave = input("Ingrese su clave: ")

        for i in range(len(usuarios)):
            if usuarios[i] == usuario and claves[i] == clave:
                acceso = True

        if acceso == True:
            print("Acceso permitido")

            
        else:
            intentos = intentos + 1
            print("Usuario o clave incorrectos")
            print("Te quedan", 3 - intentos, "intento(s)")
            if intentos == 3:
                print("Acceso denegado")
                exit()

