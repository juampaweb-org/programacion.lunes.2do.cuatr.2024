


numeros_impares = 0
numeros_pares = 0


numero = int(input("Ingrese un número (0 para detener el programa): "))

# Ejecuto el while hasta que el usuario ingrese un 0
while numero != 0:
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    # Antes de salir del while voy a preguntar nuevamente por el número.
    numero = int(input("Ingrese un número (0 para detener el programa): "))


# Imprimo los resultados
print("Numeros Pares: " + str(numeros_pares))
print("Numeros Impares: " + str(numeros_impares))

print("Fin del programa")



