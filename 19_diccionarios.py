"""Diccionarios"""


def run():
    """Ejemplos de diccionarios"""
    # mi_diccionario = {
    #     "llave1": 1,
    #     "llave2": 2,
    #     "llave3": 3,
    # }
    # print(mi_diccionario["llave1"],
    #       mi_diccionario["llave2"], mi_diccionario["llave3"])

    # ***Recorriendo un diccionario con el ciclo for***

    poblacion_paises = {
        "Colombia": 51520000,
        "Argentina": 45810000,
        "Mexico": 126700000,
    }
    # print(poblacion_paises["Argentina"])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(f"{pais} tiene {poblacion} habitantes.")


if __name__ == "__main__":
    run()
