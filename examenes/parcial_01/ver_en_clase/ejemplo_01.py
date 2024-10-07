


def generar_numeros_impares(cantidad, rango):
    """
    Genera una lista de números impares aleatorios.

    Args:
        cantidad (int): La cantidad de números impares a generar.
        rango (tupla): Un rango (minimo, maximo) dentro del cual se generarán los números.

    Returns:
        list: Una lista de números impares aleatorios.
    """
    numeros_impares = []
    minimo, maximo = rango

    while len(numeros_impares) < cantidad:
      
        numero = int(random.random() * (maximo - minimo + 1)) + minimo
        if numero % 2 != 0:
            numeros_impares.append(numero)

    return numeros_impares

