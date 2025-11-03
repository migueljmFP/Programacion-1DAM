from utiles import *
from equipos import lista_equipos

#Variables de jugadores.py
lista_jugadores = []
info_jugador = {"id": 1,
               "nombre": "Laura",
               "posicion": "Delantera",
               "equipo_id": 1,
               "activo": True}
menu_jugadores = ("Dar de alta un jugador",
                "Listar jugadores",
                "Buscar jugador por id",
                "Actualizar datos de jugadores",
                "Eliminar jugador por id",
                "Volver al menú principal")

#Funciones de jugadores.py
def ejecutar_menu_jugadores(x):
    opcion = 0
    while opcion != 6:
        print("--- MENÚ JUGADORES ---")
        mostrar_menu(menu_jugadores)

        opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
        match opcion:
            case 1:
                crear_jugador(x)
            case 2:
                listar_jugadores(x)
            case 3:
                buscar_por_id(x)
            case 4:
                actualizar_por_id(x)
            case 5:
                eliminar_por_id(x)
            case 6:
                print("Volviendo al menú principal...")
            case _:
                print("Opción no válido")

def crear_jugador(x):
    nombre = ""
    while not nombre.strip():
        nombre = input("Introduce el nombre del jugador: ")
        if not nombre.strip():
            print("El nombre no puede estar vacío.")

    posicion = ""
    while not posicion.strip():
        posicion = input("¿Cuál es la posición del jugador?: ")
        if not posicion.strip():
            print("La posición no puede estar vacía.")

    equipo_id_input = input("Introduce el ID del equipo al que pertenece el jugador: ")
    while not equipo_id_input.isdigit():
        print("El ID del equipo debe ser un número entero.")
        equipo_id_input = input("Introduce el ID del equipo al que pertenece el jugador: ")
    equipo_id = int(equipo_id_input)
    info_jugador.update({"id": generar_id(x), "nombre": nombre, "posicion": posicion, "equipo_id": equipo_id, "activo": True})
    x.append(info_jugador.copy())
    print("Jugador añadido correctamente")

def listar_jugadores(x):
    if not x:
        print("No hay jugadores para mostrar")
        return
    
    for i in x:
        print(f"{i["nombre"]} - ID: {i["id"]}, Posición: {i["posicion"]}, Actividad: {i["activo"]}")

def buscar_por_id(x):
    if not x:
        print("No se pueden buscar jugadores ya que no hay registrado ninguno")
        return
    buscar = int(input("Introduce el id del jugador que quieres buscar"))
    for i in x:
        if i["id"] == buscar:
            print(f"{i["nombre"]} - Posición: {i["posicion"]}, Actividad: {i["activo"]}")
            return
    print("No hay jugadores con ese ID")

def actualizar_por_id(x):
    if not x:
        print("No hay jugadores para actualizar")
        return
    buscar = int(input("Introduce el ID del jugador que quieras actualizar sus datos: "))
    for i in x:
        if i["id"] == buscar:
            nuevo_nombre = input("Introduce un nuevo nombre para el jugador: ")
            nueva_posicion = input("Introduce una nueva posición para el jugador: ")
            nuevo_equipo = int(input("Introduce el ID del nuevo equipo al que pertenece el jugador: "))
            
            existe_equipo = False
            for equipo in lista_equipos:
                if equipo["id"] == nuevo_equipo:
                    existe_equipo = True
            if not existe_equipo:
                print("No existe ningún equipo con ese ID.")
                return
            
            i["nombre"] = nuevo_nombre
            i["posicion"] = nueva_posicion
            i["equipo_id"] = nuevo_equipo
            print("Jugador actualizado correctamente")
            return
    print("Ningun jugador encontrado con ese ID")

def eliminar_por_id(x):
    if not x:
        print("No hay jugadores para eliminar")
        return
    eliminar = int(input("Introduce el ID del jugador que quieres eliminar: "))
    for i in x:
        if i["id"] == eliminar:
            i["activo"] = False
            print("Jugador eliminado correctamente")
            return
    print("Ningún jugador encontrado con ese ID")