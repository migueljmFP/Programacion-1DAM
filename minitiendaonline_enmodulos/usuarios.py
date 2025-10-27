#variables de usuario
usuarios = []
usuario = {"id": "",
           "nombre": "",
           "email": "",
           "activo": ""}
menu_usuario = ("Crear usuario",
                "Listar usuario",
                "Buscar usuario por id",
                "Actualizar usuario",
                "Eliminar usuario",
                "Alternar activo/inactivo",
                "Volver")

usuario_activo = 0

#funciones de usuario
def crear_usuario(n):
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in n:
        print("El nombre ya está en uso")
    else:
        email = input("Introduce un email para el usuario: ")
        if '@' and '.' not in email:
            print("El email no es válido, introduce una estructura válida con @")
        elif email in n:
            print("El email ya está registrado")
        else:
            id = int(input("Introduce un id para el usuario: "))
            if id in n:
                print("El id no se debe repetir")
            else:
                usuario.update({"id": id, "nombre": nombre, "email": email, "activo": True})
                n.append(usuario.copy())
                print(f"El usuario {nombre} añadido correctamente")

def listar_usuarios(n):
    if not n:
        print("No hay usuario para mostrar")
    else:
        for i, usuario in enumerate(n, start=1):
            print(f"{i}. {usuario['nombre']} - ID: {usuario['id']}, Email: {usuario['email']}, ¿Esta el usuario activo?: {usuario['activo']}")

def buscar_por_id_usuario(n):
    id_buscar = int(input("Introduce el ID del usuario que quieras buscar: "))
    for usuario in n:
        if usuario['id'] == id_buscar:
            print(f"Usuario encontrado: {usuario}")
            return
    print("Usuario no encontrado")

def actualizar_usuario(n):
    actualizar = int(input("Introduce el ID del usuario que quieras actualizar: "))
    for usuario in n:
        if usuario['id'] == actualizar:
            nombre_nuevo = input("Introduce un nombre nuevo: ") or usuario['nombre']
            email_nuevo = input("Introduce un email nuevo: ") or usuario['email']

            usuario['nombre'] = nombre_nuevo
            usuario['email'] = email_nuevo
            print(f"Usuario actualizado correctamente")
            return
    print("Usuario no encontrado")

def eliminar_usuario(n):
    eliminar = int(input("Introduce el id del usuario que quieras eliminar: "))
    for usuario in n:
        if usuario['id'] == eliminar:
            n.remove(usuario)
            print("El usuario ha sido eliminado correctamente")
            return
    print("Usuario no encontrado")

def cambiar_activo_usuario(n):
    cambiar = int(input("Introduce el id del usuario que quieras alternar entre activo/inactivo: "))
    for usuario in n:
        if usuario['id'] == cambiar:
            if usuario['activo'] == True:
                usuario['activo'] = False
            else:
                usuario['activo'] = True
            print("Se ha actualizado el estado de activo/inactivo")
            return
    print("Usuario no encontrado")
