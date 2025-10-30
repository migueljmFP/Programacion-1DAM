import utiles

#Variables
menú_equipos = ("Crear equipo",
                "Listar equipos",
                "Buscar equipo por id",
                "Actualizar datos de un equipo",
                "Eliminar equipo",
                "Volver")
lista_equipos = ()
info_equipo = {"id": 0,
               "nombre": "",
               "ciudad": "",
               "activo": True}

#Funciones
def crear_equipo():
    nombre = input("Introduce el nombre del equipo")
    if nombre in lista_equipos:
        print("El nombre ya está en la lista")
    else:
        ciudad = input("Introduce la ciudad a la que pertenece el equipo")
        info_equipo.update({"id": {utiles.generar_id(lista_equipos)} + 1, "nombre": {nombre}, "ciudad": {ciudad}})

def ejecutar_opcion_equipo(x):
    match x:
        case 1:
            print("hola mundo")
        case 2:
            print("hola mundo")
        case 3:
            print("hola mundo")
        case 4:
            print("hola mundo")
        case 5:
            print("hola mundo")
        case 6:
            print("Saliendo de la sección de equipos...")
        case _:
            print("No es un caracter válido")