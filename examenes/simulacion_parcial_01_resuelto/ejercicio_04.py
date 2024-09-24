"""

EJERCICIO 4
###########

 Reemplazo de vocales en palabras

Escribe un programa que:

- Reciba una lista de palabras.
- Cree una función que reemplace todas las vocales en cada palabra con un asterisco (`*`).
- Devuelva una nueva lista con las palabras modificadas.
- Imprime la lista original y la lista modificada.


Ejemplo:
Lista original: ['hola', 'python', 'examen']
Lista modificada: ['h*l*', 'pyth*n', '*x*m*n']

"""

def reemplazo_vocales(lista_palabras):
    """
    Reemplazo las vocales de las palabras de una lista por asteriscos.
    parametros:
    - lista_palabras: lista de palabras a modificar.
    return:
    - lista_modificada: lista de palabras con las vocales reemplazadas por asteriscos
    """
    lista_modificada = []
    for palabra in lista_palabras:
        palabra_modificada = ""
        for letra in palabra:
            if letra in "aeiou":
                palabra_modificada += "*"
            else:
                palabra_modificada += letra
        
        lista_modificada.append(palabra_modificada)
    return lista_modificada

lista_lenguajes = ['python', 'php', 'javascript', 'ruby', 'c++', 'go', 'nodejs']

print("Lista original:", lista_lenguajes)

lista_modificada = reemplazo_vocales(lista_lenguajes)

print("Lista modificada:", lista_modificada)

