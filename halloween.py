import random

monstruos = {"vampiro": 3,
              "momia": 2,
              "bruja": 4,
              "esqueleto": 1,
              "fantasma": 5}
objetos = ["estaca",
           "poción mágica",
           "hechizo"]
efectividad_objeto = {"estaca": 0.6,
                      "poción mágica": 0.7,
                      "hechizo": 0.8}
intentos = 3

print("¡Bienvenido a la caza de monstruos de Halloween!")

monstruo_seleccionado = random.choice(list(monstruos.keys()))

while intentos != 0:
    print(f"Tienes {intentos} intentos restantes")
    print("--- Lista de objetos ---")
    for i in objetos:
        print(i)
    objeto_usar = input("Elige un objeto: ")
    while objeto_usar not in objetos:
        print("El objeto no está en la lista")
        objeto_usar = input("Elige otro objeto: ")
    print(f"Has usado el objeto: {objeto_usar}")
    dificultad = monstruos[monstruo_seleccionado]
    efectividad = efectividad_objeto[objeto_usar]
    probabilidad_exito = efectividad - dificultad * 0,1
    intentos -= intentos
