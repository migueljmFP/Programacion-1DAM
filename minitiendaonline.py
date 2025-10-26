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
usuario_activo = 0
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
#variables de carrito/ventas
ventas = []
id_venta = 0
venta = {"id_venta": "",
         "usuario_id": "",
         "items": [("articulo_id", "cantidad", "precio_unitario" )],
         "total": ""}
menu_ventas = ("Seleccionar usuario activo",
               "Añadir artículo al carrito",
               "Quitar artículo del carrito",
               "Ver carrito",
               "Confirmar compra",
               "Historial de ventas por usuario",
               "Vaciar carrito",
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

def ejecutar_opcion_usuario(opcion):
        match opcion:
            case 1:
                crear_usuario(usuarios)
            case 2:
                listar_usuarios(usuarios)
            case 3:
                buscar_por_id_usuario(usuarios)
            case 4:
                actualizar_usuario(usuarios)
            case 5:
                eliminar_usuario(usuarios)
            case 6:
                cambiar_activo_usuario(usuarios)
            case 7:
                print("Saliendo del apartado de Usuarios...")
            case _:
                print("Número no válido")

#funciones de carrito/ventas
def usuario_activar(n):
    seleccionar = int(input("Introduce el id del usuario que quieras seleccionar para la compra: "))
    for usuario in usuarios:
        if usuario['id'] == seleccionar:
            usuario_activo = seleccionar
            id_venta += 1
            venta.update({"id_venta": id_venta, "usuario_id": usuario_activo})
            print("El usuario se ha seleccionado correctamente")
            return usuario_activo
        print("El usuario no es válido o no existe")

def añadir_articulo(n):
    if usuario_activo == 0:
        print("Primero debes seleccionar un usuario activo")
        return
    id_articulo = int(input("Introduce el ID del artículo a añadir: "))
    cantidad = int(input("Introduce la cantidad: "))
    for art in articulos:
        if art["id"] == id_articulo:
            if art["stock"] >= cantidad:
                art["stock"] -= cantidad
                venta["items"].append((id_articulo, cantidad, art["precio"]))
                print(f"Artículo '{art['nombre']}' añadido al carrito")
            else:
                print("No hay suficiente stock")
            return
    print("Artículo no encontrado")

def quitar_articulo_carrito(n):
    if not venta["items"]:
        print("El carrito está vacío")
        return
    id_articulo = int(input("Introduce el ID del artículo a quitar: "))
    for i, item in enumerate(venta["items"]):
        if item[0] == id_articulo:
            venta["items"].pop(i)
            print("Artículo eliminado del carrito")
            return
    print("Artículo no encontrado en el carrito")

def ver_carrito():
    if not venta["items"]:
        print("El carrito está vacío")
        return
    print("Carrito actual:")
    for item in venta["items"]:
        print(f"ID Artículo: {item[0]}, Cantidad: {item[1]}, Precio unitario: {item[2]}")

def confirmar_compra(n):
    if usuario_activo == 0:
        print("Primero debes seleccionar un usuario activo")
        return
    if not venta["items"]:
        print("El carrito está vacío")
        return

    total = sum(cantidad * precio for _, cantidad, precio in venta["items"])
    id_venta += 1
    venta.update({"id_venta": id_venta, "usuario_id": usuario_activo, "total": total})
    ventas.append(venta.copy())
    venta["items"].clear()
    print(f"Compra confirmada. Total: {total}")

def historial_ventas_por_usuario(n):
    id_usuario = int(input("Introduce el ID del usuario: "))
    tiene_ventas = False

    for v in n:
        if v["usuario_id"] == id_usuario:
            print(f"Venta ID: {v['id_venta']}, Total: {v['total']}, Items: {v['items']}")
            tiene_ventas = True

    if not tiene_ventas:
        print("No hay ventas para este usuario.")

def vaciar_carrito(venta):
    venta["items"].clear()
    print("Carrito vaciado")


def ejecutar_opcion_venta(opcion):
        match opcion:
            case 1:
                usuario_activar(ventas)
            case 2:
                añadir_articulo(ventas)
            case 3:
                quitar_articulo_carrito(ventas)
            case 4:
                ver_carrito(ventas)
            case 5:
                confirmar_compra(ventas)
            case 6:
                historial_ventas_por_usuario(ventas)
            case 7:
                vaciar_carrito(venta)
            case 8:
                print("Saliendo del apartado de ventas...")
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
    ejecutar_opcion_usuario(opcion)
while opcion != 8:
    mostrar_menu(menu_ventas)
    opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
    ejecutar_opcion_venta(opcion)
