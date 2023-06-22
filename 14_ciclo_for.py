"""Ciclo For"""


def run():
    """Ciclo For"""
    print(">>>")
    for contador in range(1, 11):
        print(contador)

    print(">>> Tabla del 11")
    for i in range(1, 11):
        print(f"{i} * 11 = {i*11}")


if __name__ == "__main__":
    run()
