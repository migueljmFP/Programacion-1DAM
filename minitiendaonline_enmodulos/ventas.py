import articulos
import usuarios

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

#funciones de carrito/ventas
def usuario_activar(n):
    seleccionar = int(input("Introduce el id del usuario que quieras seleccionar para la compra: "))
    for usuario in usuarios.usuarios:
        if usuario['id'] == seleccionar:
            usuarios.usuario_activo = seleccionar
            id_venta += 1
            venta.update({"id_venta": id_venta, "usuario_id": usuarios.usuario_activo})
            print("El usuario se ha seleccionado correctamente")
            return usuarios.usuario_activo
        print("El usuario no es válido o no existe")

def añadir_articulo(n):
    if usuarios.usuario_activo == 0:
        print("Primero debes seleccionar un usuario activo")
        return
    id_articulo = int(input("Introduce el ID del artículo a añadir: "))
    cantidad = int(input("Introduce la cantidad: "))
    for art in articulos.articulos:
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
    if usuarios.usuario_activo == 0:
        print("Primero debes seleccionar un usuario activo")
        return
    if not venta["items"]:
        print("El carrito está vacío")
        return

    total = sum(cantidad * precio for _, cantidad, precio in venta["items"])
    id_venta += 1
    venta.update({"id_venta": id_venta, "usuario_id": usuarios.usuario_activo, "total": total})
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
