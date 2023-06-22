# # Ejemplo 1: ejemplo básico de funciones
# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# # Ejemplo 2: Uso de parametros

# def conversacion(mensaje):
#     print("Hola")
#     print("¿Cómo estás?")
#     print(f"Elegiste la opción {mensaje}")
#     print("¡Adios!")

# opcion = int(input("Elige una opción (1, 2, 3): "))
# if opcion == 1:
#     conversacion(opcion)
# elif opcion == 2:
#     conversacion(opcion)
# elif opcion == 3:
#     conversacion(opcion)
# else:
#     print("Opción no valida")

# Ejemplo 3: retorno en una función

def suma(a, b):
    print(f"Se suman dos números: {a} y {b}")
    resultado = a + b
    return resultado

sumatoria = suma(1,4)
print(f"El resultado es: {sumatoria}")