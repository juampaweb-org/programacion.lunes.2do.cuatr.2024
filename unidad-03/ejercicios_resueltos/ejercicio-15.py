"""
15.Identificación del tipo de dato
Escribe un programa que tome una entrada del usuario
y determine su tipo de dato usando la función `type()`.
El programa debe imprimir un mensaje indicando si el dato
es un número entero, flotante, cadena de texto, etc.
"""
dato = input("Ingrese un dato: ")

try:
    # CONVERTIR EN ENTERO
    res = int(dato)
    print("Es un entero = ", res)
except ValueError:
    try:
        # CONVERTIR EN FLOAT
        res = float(dato)
        print("Es un Float = ", res)
    except ValueError:
        print("Es un string = ", dato)
range(2,17,3)
