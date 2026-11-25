from archivos.guardar_usuarios import guardar_usuarios
from autenticacion.codificar_clave import codificar_clave

def registrar_usuario(usuarios, claves, roles, rol):
    usuario = input("Ingrese el nuevo usuario: ").strip().upper()

    existe = False
    for i in range(len(usuarios)):
        if usuarios[i] == usuario:
            existe = True

    if len(usuario) < 4 or usuario.isalnum() == False:
        print("Usuario invalido, minimo 4 letras o numeros y sin espacios")
    elif existe == True:
        print("Ese usuario ya existe")
    else:
        clave = input("Ingrese la clave (minimo 6 caracteres): ")
        if len(clave) < 6:
            print("Clave muy corta, no se registro")
        else:
            usuarios.append(usuario)
            claves.append(codificar_clave(clave))
            roles.append(rol)
            guardar_usuarios(usuarios, claves, roles)
            print("Usuario registrado con rol", rol)