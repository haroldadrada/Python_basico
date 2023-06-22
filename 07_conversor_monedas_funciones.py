# Programa que convierte pesos(colombianos, argentinos o mexicanos) a dólares

def conversor(tipo_pesos, valor_dolar):
    pesos = float(input(f"¿Cuántos pesos {tipo_pesos} tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares) 
    print(f"Tienes> ${dolares} dólares.")

menu = """
Conversor de monedas a dólares 💰

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

Elige una opcion: 

"""
opcion = int(input(menu))
if opcion == 1:
    conversor("Colombianos", 4420.55)
elif opcion == 2:
    conversor("Argentinos", 215.10)
elif opcion == 3:
    conversor("Mexicanos", 18.02)
else:
    print("Opción no valida")