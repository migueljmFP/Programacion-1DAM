def mostrar_menu(x):
    for i, elemento in enumerate(x, start=1):
        print(f"{i}. {elemento}")

def generar_id(x):
    id = len(x) + 1
    return id