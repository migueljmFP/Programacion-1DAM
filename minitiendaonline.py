#definición de variables
articulos = []
articulo = {"id": "",
            "nombre": "",
            "precio": "",
            "stock": "",
            "activo": ""}
menu_principal = ("Crear artículo",
                  "Listar artículos",
                  "Buscar artículos por id",
                  "Actualizar artículo",
                  "Eliminar artículo",
                  "Alternar activo/inactivo",
                  "Salir")

#definición de funciones
def mostrar_menu(n):
    for i, elemento in enumerate(n, start=1):
        print(f"{i}. {elemento}")

def crear_articulo(n):
    nombre = input("Introduce el nombre del artículo: ")
    if nombre in articulos:
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
                id = int(input("Introduce un id al producto"))
                if id in articulos:
                    print("El id del artículo no se puede repetir")
                else:
                    articulos[articulo].append(id, nombre, precio, stock, "True")

def ejecutar_opcion(opcion):
        match opcion:
            case 1:
                crear_articulo(opcion)
            case 2:
                print("hola mundo")
            case 3:
                print("hola mundo")
            case 4:
                print("hola mundo")
            case 5:
                print("hola mundo")
            case 6:
                print("hola mundo")
            case 7:
                print("Saliendo del programa... ¡Hasta pronto!")
            case _:
                print("Número no valido")


#definición de lógica de programación
opcion = 0
while opcion != 7:
    mostrar_menu(menu_principal)
    opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
    ejecutar_opcion(opcion)