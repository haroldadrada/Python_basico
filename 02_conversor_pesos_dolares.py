# Programa que convierte pesos colombianos a dólares

pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
valor_dolar = 4458.03 # Precio del dólar en Colombia el día 12 de abril de 2023
dolares = pesos / valor_dolar
dolares = round(dolares, 2) # Función round(): Me da la cantidad de decimales que deseo después del punto
dolares = str(dolares) #Función str(): convierte un dato a texto
print(f"Tienes> ${dolares} dólares.")