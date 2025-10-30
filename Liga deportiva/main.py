import equipos
import jugadores
import calendario
import ranking
import utiles

#Variables
menu_principal = ("Gestión de equipos",
                  "Gestión de jugadores",
                  "Calendario de partidos",
                  "Resultados y clasificación",
                  "Salir")

#lógica de programación
utiles.mostrar_menu(menu_principal)
opcion = int(input("Elige una opción (Introduce el número correspondiente): "))
while opcion != 5:
    match opcion:
        case 1:
            utiles.mostrar_menu(equipos.menú_equipos)
            opcion2 = int(input("Elige una opción (Introduce el número correspondiente): "))
            while opcion2 != 6:
                equipos.ejecutar_opcion_equipo(opcion2)
        case 2:
            utiles.mostrar_menu()
            opcion3 = int(input("Elige una opción (Introduce el número correspondiente): "))