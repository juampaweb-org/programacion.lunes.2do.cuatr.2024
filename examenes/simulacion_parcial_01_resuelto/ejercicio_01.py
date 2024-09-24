
##
"""
EJERCICIO 1
###########


Escriba con sus palabras la diferencia entre un método y una función.

Y por otro lado por que pensas que es importante utilizar docstrings, en las funciones, y que es exactamente docstrings ?



"""
"""
Funciones:

Son bloques de código independientes que realizan una tarea específica.
Se pueden llamar desde cualquier parte del programa, siempre que estén definidas o sean accesibles.
Existen funciones predefinidas en muchos lenguajes (como print() o len() en Python) y también puedes crear las tuyas propias.


Métodos:

Son similares a las funciones, pero están asociados a un objeto o clase.
Se invocan sobre un objeto y suelen interactuar con los datos del objeto.
ejemplo -> variable.upper() -> upper() es un método que se invoca sobre la variable y convierte el texto en mayúsculas.


Docstrings es una cadena de texto que se coloca al principio de una función, método o clase para documentar su uso.
Va a ayudarnos en los editores de código a mostrar información sobre la función, método o clase.
La guía de estilo PEP 8 de Python define una serie de recomendaciones sobre cómo escribir docstrings (cadenas de documentación) para que el código sea más legible y consistente. A continuación te resumo los principales puntos de PEP 8 respecto a los docstrings:

ejemplo docstring:
"""

def suma(numero_uno, numero_dos):
    """
    Esta función devuelve la suma de dos números.
    
    Parámetros:
    numero_uno (int): Primer número
    numero_dos (int): Segundo número
    
    Retorna:
    int: La suma de a y numero_dos
    """
    return numero_uno + numero_dos



suma(2, 3)