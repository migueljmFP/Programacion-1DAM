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
monstruo_derrotado = False
print("¡Bienvenido a la caza de monstruos de Halloween!")

monstruo_seleccionado = random.choice(list(monstruos.keys()))
print(f"Ha aparecido {monstruo_seleccionado} con un nivel de dificultad {monstruos[monstruo_seleccionado]}")

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
    probabilidad_exito = efectividad - dificultad * 0.1
    resultado = random.random()

    if resultado < probabilidad_exito:
        print("¡Has cazado al monstruo, felicidades!")
        monstruo_derrotado = True
        intentos = 0
    else:
        print("¡El monstruo ha esquivado el ataque!")
        intentos -= 1

if monstruo_derrotado:
    print("¡Felicidades, has ganado la caza de Monstruos!")
else:
    print("¡El monstruo ha logrado escapar, has perdido!")

