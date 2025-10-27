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