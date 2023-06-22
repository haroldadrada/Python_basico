"""Códigos de ejemplos"""

menu = """
Calculadora Básica.

1. Suma
2. Resta
3. Multiplicación
4. División

Elige una opcion: 
"""


def suma(numero_uno, numero_dos):
    """Función para la suma"""
    sumar = numero_uno + numero_dos
    print(f"El resultado es: {numero_uno} + {numero_dos} = {sumar}")


def resta(numero_uno, numero_dos):
    """Función para la resta"""
    restar = numero_uno - numero_dos
    print(f"El resultado es: {numero_uno} - {numero_dos} = {restar}")


def multiplicacion(numero_uno, numero_dos):
    """Función para la multiplicación"""
    multiplicar = numero_uno * numero_dos
    print(f"El resultado es: {numero_uno} * {numero_dos} = {multiplicar}")


def division(numero_uno, numero_dos):
    """Función para la división"""
    dividir = numero_uno / numero_dos
    print(f"El resultado es: {numero_uno} / {numero_dos} = {dividir}")


def run():
    """Calculadora"""

    opcion = int(input(menu))
    numero_uno = int(input("Ingresa el primer valor: "))
    numero_dos = int(input("Ingresa el segundo valor: "))
    if opcion == 1:
        suma(numero_uno, numero_dos)
    elif opcion == 2:
        resta(numero_uno, numero_dos)
    elif opcion == 3:
        multiplicacion(numero_uno, numero_dos)
    elif opcion == 4:
        division(numero_uno, numero_dos)
    else:
        print("Opción no valida")


if __name__ == "__main__":
    run()
