"""Break y Continue en Python"""


def run():
    """Ejemplos de break y continue"""
    # # Ejemplo 1: Imprime los números pares hasta el 99
    # for contador in range(100):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # # Ejemplo 2: Cortar ciclo cuando llegue a un número en particular. rango(1000)
    # for i in range(1000):
    #     print(i)
    #     if i == 323:
    #         break

    # Ejemplo 3: cuando encuentre al caracter "o" en la cadena de caracteres, corta el ciclo
    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == "__main__":
    run()
