import articulos
import usuarios
import ventas

def ejecutar_opcion_articulo(opcion):
        match opcion:
            case 1:
                articulos.crear_articulo(articulos.articulos)
            case 2:
                articulos.listar_articulos(articulos.articulos)
            case 3:
                articulos.buscar_por_id_articulo(articulos.articulos)
            case 4:
                articulos.actualizar_articulo(articulos.articulos)
            case 5:
                articulos.eliminar_articulo(articulos.articulos)
            case 6:
                articulos.cambiar_activo_articulo(articulos.articulos)
            case 7:
                print("Saliendo del apartado de productos...")
            case _:
                print("Número no válido")

def ejecutar_opcion_usuario(opcion):
        match opcion:
            case 1:
                usuarios.crear_usuario(usuarios.usuarios)
            case 2:
                usuarios.listar_usuarios(usuarios.usuarios)
            case 3:
                usuarios.buscar_por_id_usuario(usuarios.usuarios)
            case 4:
                usuarios.actualizar_usuario(usuarios.usuarios)
            case 5:
                usuarios.eliminar_usuario(usuarios.usuarios)
            case 6:
                usuarios.cambiar_activo_usuario(usuarios.usuarios)
            case 7:
                print("Saliendo del apartado de Usuarios...")
            case _:
                print("Número no válido")

def ejecutar_opcion_venta(opcion):
        match opcion:
            case 1:
                ventas.usuario_activar(ventas.ventas)
            case 2:
                ventas.añadir_articulo(ventas.ventas)
            case 3:
                ventas.quitar_articulo_carrito(ventas.ventas)
            case 4:
                ventas.ver_carrito(ventas.ventas)
            case 5:
                ventas.confirmar_compra(ventas.ventas)
            case 6:
                ventas.historial_ventas_por_usuario(ventas.ventas)
            case 7:
                ventas.vaciar_carrito(ventas.venta)
            case 8:
                print("Saliendo del apartado de ventas...")
            case _:
                print("Número no válido")

def mostrar_menu(n):
    for i, elemento in enumerate(n, start=1):
        print(f"{i}. {elemento}")
#definición de lógica de programación
opcion = 0
while opcion != 7:
    mostrar_menu(articulos.menu_articulos)
    opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
    ejecutar_opcion_articulo(opcion)
opcion = 0
while opcion != 7:
    mostrar_menu(usuarios.menu_usuario)
    opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
    ejecutar_opcion_usuario(opcion)
while opcion != 8:
    mostrar_menu(ventas.menu_ventas)
    opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
    ejecutar_opcion_venta(opcion)
