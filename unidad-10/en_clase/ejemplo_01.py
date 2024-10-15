




# Ejemplo de uso de try except


try:
    numero = input("Ingresa un número natural: ")
    print("El reciproco de {} es {}".format(numero, 1/numero))

except ZeroDivisionError:
    # Acá tenemos el bloque de código que se ejecutará si se produce una excepción de tipo ZeroDivisionError
    print("No se puede dividir por cero")
    # Fin del bloque de código

except ValueError:
    # Acá tenemos el bloque de código que se ejecutará si se produce una excepción de tipo ValueError
    print("Debes ingresar un número")
    # Fin del bloque de código


# Luego de los bloques de manejo de excepciones, podemos seguir con el flujo normal del programa
print("Fin del programa")

