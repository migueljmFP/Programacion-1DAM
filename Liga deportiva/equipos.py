from utiles import *

#Variables de equipos.py
lista_equipos = []
info_equipo = {"id": 1,
               "nombre": "Tiburones",
               "ciudad": "Getafe",
               "activo": True}
menu_equipos = ("Crear equipo",
                "Listar equipos",
                "Buscar equipo por id",
                "Actualizar datos de equipos",
                "Eliminar equipo por id",
                "Volver al menú principal")

#Funciones de equipos.py
def ejecutar_menu_equipo(x):
    opcion = 0
    while opcion != 6:
        print("--- MENÚ EQUIPOS ---")
        mostrar_menu(menu_equipos)

        opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
        match opcion:
            case 1:
                crear_equipo(x)
            case 2:
                listar_equipos(x)
            case 3:
                buscar_por_id(x)
            case 4:
                actualizar_por_id(x)
            case 5:
                eliminar_por_id(x)
            case 6:
                print("Volviendo al menú principal...")
            case _:
                print("Opción no válida")

def crear_equipo(x):
    nombre = ""
    while not nombre.strip():
        nombre = input("Introduce un nombre para el equipo: ")
        if not nombre.strip():
            print("El nombre no puede estar vacío.")
    if any(i["nombre"] == nombre for i in x):
        print("El nombre ya está en uso")
        return
    ciudad = ""
    while not ciudad.strip():
        ciudad = input("¿En qué ciudad se ubica el equipo?: ")
        if not ciudad.strip():
            print("La ciudad no puede estar vacía.")

    info_equipo.update({"id": generar_id(x), "nombre": nombre, "ciudad": ciudad, "activo": True})
    x.append(info_equipo.copy())
    print("El equipo ha sido añadido correctamente")

def listar_equipos(x):
    if not x:
        print("No hay equipos para mostrar")
        return
    else:
        for i in x:
            if i["activo"] == True:
                print(f"{i["nombre"]} - ID: {i["id"]}, Ciudad: {i["ciudad"]}, Actividad: {i["activo"]}")

def buscar_por_id(x):
    if not x:
        print("No se pueden buscar equipos ya que no existen equipos")
        return
    buscar = int(input("Introduce el id del equipo que quieres buscar"))
    for i in x:
        if i["id"] == buscar:
            print(f"{i["nombre"]} - Ciudad: {i["ciudad"]}, Actividad: {i["activo"]}")
            return
    print("No hay equipos con ese ID")

def actualizar_por_id(x):
    if not x:
        print("No hay equipos para actualizar")
        return
    buscar = int(input("Introduce el ID del equipo que quieras actualizar sus datos: "))
    for i in x:
        if i["id"] == buscar:
            nuevo_nombre = input("Introduce un nuevo nombre para el equipo: ")
            nueva_ciudad = input("Introduce una nueva ciudad para el equipo: ")
            i["nombre"] = nuevo_nombre
            i["ciudad"] = nueva_ciudad
            print("Equipo actualizado correctamente")
            return
    print("Ningun equipo encontrado con ese ID")

def eliminar_por_id(x):
    if not x:
        print("No hay equipos para eliminar")
        return
    eliminar = int(input("Introduce el ID del equipo que quieres eliminar: "))
    for i in x:
        if i["id"] == eliminar:
            i["activo"] = False
            print("Equipo eliminado correctamente")
            return
    print("Ningún equipo encontrado con ese ID")