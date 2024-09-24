

"""
EJERCICIO 2
###########


Combina dos listas: Escribe una función que combine dos listas en una sola lista.
Ejemplo: [1, 2, 3] y [4, 5, 6] se convierte en [1, 2, 3, 4, 5, 6].

"""


def get_lista_unificada(lista_1, lista_2):
    """
    Me va a devolver una lista unificada de dos listas.
    parametros:
    lista_1: list
    lista_2: list
    return: list
    """
    return lista_1 + lista_2



lista_pares = [2, 4, 6, 8]
lista_impares = [1, 3, 5, 7]

lista_unificada = get_lista_unificada(lista_pares, lista_impares)

print(lista_unificada)



