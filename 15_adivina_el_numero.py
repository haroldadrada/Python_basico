"""Video Juego"""

import random


def run():
    """Juego: adivina el número"""
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elije un número entre 1 y 100: "))
    while numero_aleatorio != numero_elegido:
        if numero_aleatorio > numero_elegido:
            print("Escoge un número más grande")
        else:
            print("Escoge un número más pequeño")
        numero_elegido = int(input("Elije otro número: "))
    print(f"Ganaste, con el número {numero_aleatorio}")


if __name__ == "__main__":
    run()
