# palabra = str(input("Ingresa una palabra: "))
# palabra = palabra.replace(" ","").lower().strip()

# if palabra == palabra[::-1]:
#     print("Es palíndromo")
# else:
#     print("No es palíndromo")

def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower().strip()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = str(input("Escribe una palabra: "))
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == "__main__":
    run()