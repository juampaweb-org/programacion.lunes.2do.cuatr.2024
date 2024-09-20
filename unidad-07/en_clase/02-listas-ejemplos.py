

# Podemos hacer una función que le pasemos una lista de numeros y haga una suma de todos los elementos


def sumar_numeros_lista( lista_nros ):
    suma = 0
    for nro in lista_nros:
        suma += nro
    return suma

# Ejemplo de uso
lista_de_numeros = [12, 37, 5, 42, 8, 3]
print(sumar_numeros_lista(lista_de_numeros))  # 107

