def tablas_multiplicar(numero_tabla):
    print(f"La tabla de Multiplicar del {numero_tabla} es la siguiente: ")
    for i in range(1, 11):
        print(f"{i} x {numero_tabla} = {i*numero_tabla}")


def run():
    numero_tabla = int(input("¿Qué tabla de Multiplicar deseas ver?: "))
    tablas_multiplicar(numero_tabla)


if __name__ == "__main__":
    run()