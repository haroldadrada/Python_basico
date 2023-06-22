# Programa que convierte Dólares en Pesos Colombianos

dolares = float(input("¿Cuántos Dólares tienes?: "))
valor_dolar = 4458.03
pesos = dolares*valor_dolar
pesos = round(pesos, 2)
pesos = str(pesos)
print(f"Tienes ${pesos} pesos.")