import numpy as np
import random
import pickle

#Creación del tablero donde se ubicarán los barcos (no visible para el jugador)
tablero = np.zeros((20, 20), dtype= int)

barcos = [2, 3, 4]

#Menú de guardado (para más adelante)
menu = ["Guardar",
        "Salir"]
#Colocación de los barcos en el tablero
def colocar_barcos(tablero, barcos):
    for tamaño in barcos:
        colocado = False
        while colocado == False:
            orientacion = random.randint(0, 1)
            #Si el barco se coloca vertical u horizontalmente
            if orientacion == 0:
                fila = random.randint(0, 19)
                columna = random.randint(0, 20 - tamaño)

                if np.all(tablero[fila, columna:columna+tamaño] == 0):
                    tablero[fila, columna:columna+tamaño] = 1
                    colocado = True
            else:
                fila = random.randint(0, 20 - tamaño)
                columna = random.randint(0, 19)

                if np.all(tablero[fila:fila + tamaño, columna] == 0):
                    tablero[fila:fila + tamaño, columna] = 1
                    colocado = True

#Datos de guardado y cargar partida (si existe)
def guardar_partida(nombre_archivo):
    with open(nombre_archivo, "wb") as archivo:
        pickle.dump({
            "tablero": tablero,
            "tablero_jugador": tablero_jugador,
            "intentos": intentos,
            "barcos_restantes": barcos_restantes
            }, archivo)
        
def cargar_partida(nombre_archivo):
    with open(nombre_archivo, "rb") as archivo:
        datos = pickle.load(archivo)
    print("Datos cargados correctamente")
    return datos["tablero"], datos["tablero_jugador"], datos["intentos"], datos["barcos_restantes"]

respuesta = input("¿Quieres cargar una partida? Sí o No: ")
if respuesta == "Sí":
    tablero, tablero_jugador, intentos, barcos_restantes = cargar_partida("partida_guardada.sav")
else:
    colocar_barcos(tablero, barcos)
    tablero_jugador = np.full((20, 20), "~")
    intentos = 0
    barcos_restantes = sum(barcos)


#Lógica del juegp

print("Bienvenido a Hundir la Flota")
print("El tablero es de 20x20. Las posiciones de fila y columna están entre 0 y 19")

#Elegir la columna y la fila
while barcos_restantes > 0:
    eleccion = input("Escribe 'jugar' para empezar la partida, o 'salir' para salir: ")
    if eleccion == "salir":
        print("Saliendo del juego...")
        barcos_restantes = 0
    elif eleccion == "jugar":
        fila_input = input("Fila: ")
        columna_input = input("Columna: ")

        #Verificar si son caracteres válidos (dígitos)
        if fila_input.isdigit() and columna_input.isdigit():
            fila = int(fila_input)
            columna = int(columna_input)

            #Verificación de si la posición está en el tablero
            if 0 <= fila <= 19 and 0 <= columna <= 19:
                intentos += 1

                #Barco tocado o no tocado
                if tablero[fila, columna] == 1:
                    print("¡Tocado!")
                    tablero_jugador[fila, columna] = "X"
                    tablero[fila, columna] = 0
                    barcos_restantes -= 1
                    guardar_partida("partida_guardada.sav")
                    print("Partida guardada")
                    #Todos los barcos destruidos
                    if barcos_restantes == 0:
                        print(f"¡Felicidades, has hundido todos los barcos con un total de {intentos} intentos!")

                elif tablero_jugador[fila, columna] in ["X", "O"]:
                    print("Ya probaste esta posición")
                else:
                    print("¡Agua!")
                    tablero_jugador[fila, columna] = "O"
                    guardar_partida("partida_guardada.sav")
                    print("Partida guardada")
            else:
                print("Posición fuera del tablero")
        else:
            print("Número no válido")

        #Mostrar como va el tablero
        for fila_tablero in tablero_jugador:
            print(" ".join(fila_tablero.tolist()))