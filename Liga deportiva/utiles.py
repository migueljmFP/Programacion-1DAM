def mostrar_menu(x):
    print("=== MENÚ ===")
    for i, elemento in enumerate(x, start=1):
        print(f"{i}. {elemento}")
    opcion = int(input("Escoge una opción (Introduce el número correspondiente): "))
    return opcion

def generar_id(x):
    id = len(x) + 1
    return id