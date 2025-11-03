from utiles import *
from calendario import lista_partidos
from equipos import lista_equipos

#Variables de ranking.py
menu_ranking = ("Registrar resultado de partido",
                     "Mostrar clasificación general",
                     "Mostrar estadísticas por equipo",
                     "Volver al menú principal")

#Funciones de ranking.py
def ejecutar_menu_ranking(x):
    opcion = 0
    while opcion != 4:
        print("--- MENÚ ESTADÍSTICAS Y RESULTADOS ---")
        mostrar_menu(menu_ranking)

        opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
        match opcion:
            case 1:
                registrar_resultado(x)
            case 2:
                mostrar_clasificacion(x)
            case 3:
                mostrar_estadisticas_equipo(x)
            case 4:
                print("Volviendo al menú principal...")
            case _:
                print("Opción no válida")

def registrar_resultado(x):
    tiene_pendientes = False
    for p in x:
        if not p["jugado"]:
            tiene_pendientes = True

    if not tiene_pendientes:
        print("No hay partidos pendientes para registrar.")
        return

    print("Partidos pendientes:")
    for p in x:
        if not p["jugado"]:
            print(f"ID: {p['id']} | Jornada {p['jornada']} | {p['local_id']} vs {p['visitante_id']}")

    partido_id = int(input("Introduce el ID del partido que deseas registrar: "))
    encontrado = False
    for p in x:
        if p["id"] == partido_id and not p["jugado"]:
            goles_local = int(input("Introduce los goles del equipo local: "))
            goles_visitante = int(input("Introduce los goles del equipo visitante: "))

            if goles_local < 0 or goles_visitante < 0:
                print("Los goles no pueden ser negativos.")
                return

            p["resultado"] = {
                "goles_local": goles_local,
                "goles_visitante": goles_visitante
            }
            p["jugado"] = True
            print("Resultado registrado correctamente.")
            encontrado = True
    if not encontrado:
        print("No se encontró ningún partido pendiente con ese ID.")

def mostrar_clasificacion(x):
    tabla = {}

    for p in x:
        if p["jugado"] and p["resultado"] is not None:
            lid = p["local_id"]
            vid = p["visitante_id"]
            gl = p["resultado"]["goles_local"]
            gv = p["resultado"]["goles_visitante"]

            if lid not in tabla:
                tabla[lid] = {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "DG": 0, "PTS": 0}
            if vid not in tabla:
                tabla[vid] = {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "DG": 0, "PTS": 0}

            tabla[lid]["PJ"] += 1
            tabla[vid]["PJ"] += 1
            tabla[lid]["GF"] += gl
            tabla[lid]["GC"] += gv
            tabla[vid]["GF"] += gv
            tabla[vid]["GC"] += gl

            if gl > gv:
                tabla[lid]["G"] += 1
                tabla[vid]["P"] += 1
                tabla[lid]["PTS"] += 3
            elif gl < gv:
                tabla[vid]["G"] += 1
                tabla[lid]["P"] += 1
                tabla[vid]["PTS"] += 3
            else:
                tabla[lid]["E"] += 1
                tabla[vid]["E"] += 1
                tabla[lid]["PTS"] += 1
                tabla[vid]["PTS"] += 1

    for eid in tabla:
        tabla[eid]["DG"] = tabla[eid]["GF"] - tabla[eid]["GC"]

    ordenados = []
    for eid in tabla:
        ordenados.append((eid, tabla[eid]))
    ordenados.sort(key=lambda x: x[1]["PTS"], reverse=True)

    print("--- CLASIFICACIÓN GENERAL ---")
    print("Equipo | PJ | G | E | P | GF | GC | DG | PTS")
    for eid, stats in ordenados:
        nombre = "Desconocido"
        for e in lista_equipos:
            if e["id"] == eid:
                nombre = e["nombre"]
        print(f"{nombre} | {stats['PJ']} | {stats['G']} | {stats['E']} | {stats['P']} | {stats['GF']} | {stats['GC']} | {stats['DG']} | {stats['PTS']}")

def mostrar_estadisticas_equipo(x):
    equipo_id = int(input("Introduce el ID del equipo para ver sus estadísticas: "))
    nombre = None
    for e in lista_equipos:
        if e["id"] == equipo_id:
            nombre = e["nombre"]
    if not nombre:
        print("No existe ningún equipo con ese ID.")
        return

    PJ = G = E = P = GF = GC = PTS = 0

    for p in x:
        if p["jugado"] and p["resultado"] is not None:
            gl = p["resultado"]["goles_local"]
            gv = p["resultado"]["goles_visitante"]

            if p["local_id"] == equipo_id or p["visitante_id"] == equipo_id:
                PJ += 1
                if p["local_id"] == equipo_id:
                    GF += gl
                    GC += gv
                    if gl > gv:
                        G += 1
                        PTS += 3
                    elif gl < gv:
                        P += 1
                    else:
                        E += 1
                        PTS += 1
                else:
                    GF += gv
                    GC += gl
                    if gv > gl:
                        G += 1
                        PTS += 3
                    elif gv < gl:
                        P += 1
                    else:
                        E += 1
                        PTS += 1

    print(f"Estadísticas de {nombre}")
    print(f"PJ: {PJ} | G: {G} | E: {E} | P: {P} | GF: {GF} | GC: {GC} | PTS: {PTS}")
