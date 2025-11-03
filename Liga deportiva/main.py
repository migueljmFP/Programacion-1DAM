import equipos
import jugadores
from utiles import *
import calendario
import ranking

#Variables de main.py
menu_principal = ("Gestión de equipos",
                  "Gestión de jugadores",
                  "Calendario de partidos",
                  "Resultados y clasificación",
                  "Salir")
#funcion principal
def main():
    opcion = 0
    while opcion != 5:
        print("--- MENÚ PRINCIPAL ---")
        mostrar_menu(menu_principal)
        opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))

        match opcion:
            case 1:
                equipos.ejecutar_menu_equipo(equipos.lista_equipos)
            case 2:
                jugadores.ejecutar_menu_jugadores(jugadores.lista_jugadores)
            case 3:
                calendario.ejecutar_menu_calendario(calendario.lista_partidos)
            case 4:
                ranking.ejecutar_menu_ranking(ranking.lista_partidos)
            case 5:
                print("Saliendo del programa, ¡Hasta pronto!")
            case _:
                print("Opción no válida")
#Lógica de programación 
main()