from utiles import *
from equipos import lista_equipos
from datetime import datetime

#variables de calendario.py
lista_partidos = []
info_partido = {"id": 1, "jornada": 3,
                "local_id": 1, "visitante_id": 1,
                "fecha": "2025-11-22", "hora": "18:30",
                "jugado": False, "resultado": None}

menu_calendario = ("Crear partido",
                   "Listar partidos",
                   "Reprogramar partido",
                   "Eliminar partido",
                   "Volver al menú principal")

#funciones de calendario.py
def ejecutar_menu_calendario(x):
    opcion = 0
    while opcion != 5:
        print("--- MENÚ CALENDARIO Y PARTIDOS ---")
        mostrar_menu(menu_calendario)

        opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
        match opcion:
            case 1:
                crear_partido(x)
            case 2:
                listar_partidos(x)
            case 3:
                reprogramar_partido(x)
            case 4:
                eliminar_partido(x)
            case 5:
                print("Volviendo al menú principal...")
            case _:
                print("Opción no válida")

def crear_partido(x):
    jornada = int(input("Introduce el número de jornada: "))
    if jornada < 1:
        print("La jornada debe ser mayor o igual a 1.")
        return

    local_id = int(input("Introduce el ID del equipo local: "))
    visitante_id = int(input("Introduce el ID del equipo visitante: "))

    if local_id == visitante_id:
        print("El equipo local y visitante no pueden ser el mismo.")
        return

    local_activo = False
    visitante_activo = False
    for e in lista_equipos:
        if e["id"] == local_id and e["activo"]:
            local_activo = True
        if e["id"] == visitante_id and e["activo"]:
            visitante_activo = True

    if not local_activo or not visitante_activo:
        print("Ambos equipos deben estar activos.")
        return

    fecha = input("Introduce la fecha del partido (YYYY-MM-DD): ")
    hora = input("Introduce la hora del partido (HH:MM): ")

    formato_valido = (
        len(fecha) == 10 and fecha[4] == "-" and fecha[7] == "-" and
        len(hora) == 5 and hora[2] == ":"
    )

    if not formato_valido:
        print("Formato de fecha u hora inválido.")
        return

    datetime.strptime(fecha, "%Y-%m-%d")
    datetime.strptime(hora, "%H:%M")

    info_partido.update({
        "id": generar_id(x),
        "jornada": jornada,
        "local_id": local_id,
        "visitante_id": visitante_id,
        "fecha": fecha,
        "hora": hora,
        "jugado": False,
        "resultado": None
    })
    x.append(info_partido.copy())
    print("Partido creado correctamente.")

def listar_partidos(x):
    if not x:
        print("No hay partidos para mostrar.")
        return

    filtro = input("¿Deseas filtrar por jornada? (s/n): ").lower()
    if filtro == "s":
        jornada = int(input("Introduce el número de jornada: "))
        partidos = []
        for p in x:
            if p["jornada"] == jornada:
                partidos.append(p)
    else:
        partidos = x

    if not partidos:
        print("No hay partidos que coincidan con el filtro.")
        return

    for p in partidos:
        local = "Desconocido"
        visitante = "Desconocido"
        for e in lista_equipos:
            if e["id"] == p["local_id"]:
                local = e["nombre"]
            if e["id"] == p["visitante_id"]:
                visitante = e["nombre"]
        if p["resultado"]:
            resultado = f"{p['resultado']['goles_local']} - {p['resultado']['goles_visitante']}"
        else:
            resultado = "Pendiente"
        print(f"ID: {p['id']} | Jornada {p['jornada']} | {local} vs {visitante} | {p['fecha']} {p['hora']} | Resultado: {resultado}")

def reprogramar_partido(x):
    if not x:
        print("No hay partidos para reprogramar.")
        return

    buscar = int(input("Introduce el ID del partido a reprogramar: "))
    for p in x:
        if p["id"] == buscar:
            if p["jugado"]:
                print("No se puede reprogramar un partido ya jugado.")
                return

            nueva_fecha = input("Introduce la nueva fecha (YYYY-MM-DD): ")
            nueva_hora = input("Introduce la nueva hora (HH:MM): ")

            formato_valido = (
                len(nueva_fecha) == 10 and nueva_fecha[4] == "-" and nueva_fecha[7] == "-" and
                len(nueva_hora) == 5 and nueva_hora[2] == ":"
            )

            if not formato_valido:
                print("Formato de fecha u hora inválido.")
                return

            datetime.strptime(nueva_fecha, "%Y-%m-%d")
            datetime.strptime(nueva_hora, "%H:%M")

            p["fecha"] = nueva_fecha
            p["hora"] = nueva_hora
            print("Partido reprogramado correctamente.")
            return

    print("No se encontró ningún partido con ese ID.")

def eliminar_partido(x):
    if not x:
        print("No hay partidos para eliminar.")
        return

    eliminar = int(input("Introduce el ID del partido que deseas eliminar: "))
    for i in range(len(x)):
        if x[i]["id"] == eliminar:
            if x[i]["jugado"]:
                print("No se puede eliminar un partido ya jugado.")
                return
            x.pop(i)
            print("Partido eliminado correctamente.")
            return

    print("No se encontró ningún partido con ese ID.")