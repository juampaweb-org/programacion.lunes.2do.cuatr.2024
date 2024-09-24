
"""
EJERCICIO 3
###########


Elimina duplicados: Crea una función que elimine los elementos duplicados de una lista.
Ejemplo: [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"] ---->>  se convierte en [1, 2, 3, 4, "Pedro", "Florencia", "Ana"].

"""


def eliminar_duplicados(lista_original):
    """
    Elimina los elementos duplicados de una lista.
    parametros:
    lista: list
    return: list
    """
    lista_sin_duplicados = []
    
    for elemento in lista_original:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    
    return lista_sin_duplicados


lista_original = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro", 2, 10]

lista_sin_duplicados = eliminar_duplicados(lista_original)

print(lista_sin_duplicados)

