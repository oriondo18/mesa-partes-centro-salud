import hashlib

def codificar_clave(clave):
    codigo = hashlib.sha256(clave.encode("utf-8")).hexdigest()
    return codigo[:10]