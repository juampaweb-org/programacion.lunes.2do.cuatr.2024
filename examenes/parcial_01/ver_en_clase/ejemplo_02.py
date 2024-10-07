

def buscar_elemento(lista, elemento):
    """
    Busca un elemento en una lista y devuelve su índice.

    Args:
        lista (list): La lista en la que se buscará el elemento.
        elemento (int/float): El elemento que se desea buscar.

    Returns:
        int/str: El índice del elemento si se encuentra.
    """
    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return indice



