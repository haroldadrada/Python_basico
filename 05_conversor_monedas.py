# Programa que convierte pesos(colombianos, argentinos o mexicanos) a dólares

menu = """
Conversor de monedas a dólares 💰

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

Elige una opcion: 

"""
opcion = int(input(menu))
if opcion == 1:
    pesos = float(input("¿Cuántos pesos Colombianos tienes?: "))
    valor_dolar = 4419.73 # Precio del dólar en Colombia el día 13 de abril de 2023
    dolares = pesos / valor_dolar
    dolares = round(dolares, 3) 
    dolares = str(dolares) 
    print(f"Tienes> ${dolares} dólares.")
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos Argentinos tienes?: "))
    valor_dolar = 214.68 # Precio del dólar en Argentina el día 13 de abril de 2023
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares) 
    print(f"Tienes> ${dolares} dólares.")
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos Mexicanos tienes?: "))
    valor_dolar = 18.01 # Precio del dólar en México el día 13 de abril de 2023
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares) 
    print(f"Tienes> ${dolares} dólares.")
else:
    print("Opción no valida")