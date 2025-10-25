#definición de variables
#variables de articulos
articulos = []
articulo = {"id": "",
            "nombre": "",
            "precio": "",
            "stock": "",
            "activo": ""}
menu_articulos = ("Crear artículo",
                  "Listar artículos",
                  "Buscar artículos por id",
                  "Actualizar artículo",
                  "Eliminar artículo",
                  "Alternar activo/inactivo",
                  "Salir")
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
#definición de funciones
def mostrar_menu(n):
    for i, elemento in enumerate(n, start=1):
        print(f"{i}. {elemento}")
#funciones de articulos
def crear_articulo(n):
    nombre = input("Introduce el nombre del artículo: ")
    if nombre in n:
        print("¡El nombre ya está en la lista de artículos!")
    else:
        precio = float(input("Introduce un precio para el artículo (con decimales): "))
        if precio <= 0:
            ("El precio debe ser positivo (mayor que 0)")
        else:
            stock = int(input("Introduce el número de unidades: "))
            if stock <= 0:
                print("El stock debe ser entero (mayor que 0, y sin decimales)")
            else:
                id = int(input("Introduce un id al producto: "))
                if id in n:
                    print("El id del artículo no se puede repetir")
                else:
                    articulo.update({"id": id, "nombre": nombre,"precio": precio,"stock": stock,"activo": True})
                    n.append(articulo.copy())
                    print(f"El artículo '{nombre}' fue añadido correctamente")

def listar_articulos(n):
    if not n:
        print("No hay artículos para mostrar")
    for i, articulo in enumerate(n, start=1):
        print(f"{i}. {articulo['nombre']} - ID: {articulo['id']}, Precio: {articulo['precio']}, Stock: {articulo['stock']}, ¿Está activo?: {articulo['activo']}")

def buscar_por_id_articulo(n):
    id_buscar = int(input("Introduce el id del artículo que quieres buscar: "))
    for articulo in n:
        if articulo['id'] == id_buscar:
            print(f"Artículo encontrado: {articulo}")
            return
    print("Artículo no encontrado")

def actualizar_articulo(n):
    actualizar = int(input("Introduce el id del artículo que quieras actualizar: "))
    for articulo in n:
        if articulo['id'] == actualizar:
            nombre_nuevo = input("Introduce un nuevo nombre: ") or articulo['nombre']
            precio_nuevo = float(input("Introduce un nuevo precio (con decimales): ")) or articulo['precio']
            stock_nuevo = int(input("Introduce una nueva cantidad: ")) or articulo['stock']

            articulo['nombre'] = nombre_nuevo
            articulo['precio'] = precio_nuevo
            articulo['stock'] = stock_nuevo

            print("Artículo actualizado correctamente")
            return
        
    print("Artículo no encontrado")

def eliminar_articulo(n):
    eliminar = input("Introduce el nombre del artículo que quieres eliminar: ")
    for i in n:
        if articulo['nombre'] == eliminar:
            n.remove(articulo)
            print("El artículo ha sido eliminado correctamente")
            return
    print("Artículo no encontrado")

def cambiar_activo_articulo(n):
    cambiar = input("Introduce el nombre del artículo que quieras alternar entre activo e inactivo: ")
    for articulo in n:
        if articulo['nombre'] == cambiar:
            if articulo['activo'] == False:
                articulo['activo'] = True
            else:
                articulo['activo'] = False
            print("Se ha actualizado el estado activo/inactivo")
            return
    print("Artículo no encontrado")

def ejecutar_opcion_articulo(opcion):
        match opcion:
            case 1:
                crear_articulo(articulos)
            case 2:
                listar_articulos(articulos)
            case 3:
                buscar_por_id_articulo(articulos)
            case 4:
                actualizar_articulo(articulos)
            case 5:
                eliminar_articulo(articulos)
            case 6:
                cambiar_activo_articulo(articulos)
            case 7:
                print("Saliendo del apartado de productos...")
            case _:
                print("Número no válido")

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

def ejecutar_opcion_usuario(n):
        match opcion:
            case 1:
                crear_usuario(n)
            case 2:
                listar_usuarios(n)
            case 3:
                buscar_por_id_usuario(n)
            case 4:
                actualizar_usuario(n)
            case 5:
                eliminar_usuario(n)
            case 6:
                cambiar_activo_usuario(n)
            case 7:
                print("Saliendo del apartado de Usuarios...")
            case _:
                print("Número no válido")

#definición de lógica de programación
opcion = 0
while opcion != 7:
    mostrar_menu(menu_articulos)
    opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
    ejecutar_opcion_articulo(opcion)
opcion = 0
while opcion != 7:
    mostrar_menu(menu_usuario)
    opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
    ejecutar_opcion_usuario(usuarios)
