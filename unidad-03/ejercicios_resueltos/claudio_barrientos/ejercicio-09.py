"""
9. Pregunta al usuario que ingrese un número.
Si es positivo, imprime "El número es positivo".
Si es negativo, imprime "El número es negativo".
Si es cero, imprime "El número es cero".
"""

num = int(input("Ingrese un número: "))

if num > 0:
    print("El número es positivo")
else:
    if num < 0:
        print("El número es negativo")
    else:
        print("El número es cero")
