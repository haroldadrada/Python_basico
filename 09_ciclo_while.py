def run():
    # *** Ciclo While (mientras) ***
    # Ejemplo 1: Imprimir las potencias de 2 hasta que pase de mil
    LIMITE = 1000 #Es una constante(no varia), por tanto va en mayusculas
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(f"2 elevado a la {contador} es: {potencia_2}")
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()