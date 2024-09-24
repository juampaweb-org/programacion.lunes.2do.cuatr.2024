

"""
EJERCICIO 5
###########


Escribe una función llamada es_primo que reciba un número entero como parámetro y determine si es primo o no.
La función debe utilizar un bucle while para verificar si el número es divisible por algún otro número menor que él mismo (excluyendo 1 y el propio número). Si encuentra un divisor, debe retornar False, indicando que el número no es primo. Si no encuentra ningún divisor, debe retornar True, indicando que el número es primo.

"""

def es_primo( numero ):
    """
    Me va retornar True si el número es primo, False si no lo es.
    parametros:
    numero: int
    return: bool
    """
    if numero == 1:
        return False
    
    numero_original = numero
    while( numero > 2 ):
        numero -= 1
        if numero_original % numero == 0:
            return False
    return True


# Pruebas
print( es_primo( 1 ) ) # False
print( es_primo( 2 ) ) # True
print( es_primo( 19 ) ) # True
print( es_primo( 66 ) ) # False

if (es_primo(3)):
    print("El número es primo")