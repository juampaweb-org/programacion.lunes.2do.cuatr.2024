total = 1523

# Uso de los operadores de comparación (and, or, not) en una estructura condicional if
if total > 1000:
    print("El total es mayor a 1000")


# Inicialización de una variable 'i' con valor 0 para utilizarla en un bucle while
i = 0

# Ejemplo de un bucle while que se ejecuta mientras la condición sea verdadera (i < 5)
while i < 5:
    print(i)  
    i += 1    # Incrementa el valor de 'i' en 1 en cada iteración del bucle
else:
    # Una vez que la condición del bucle while (i < 5) se vuelve False, por lo tanto entra acá. Al bloque del else.
    i = i + 1
    if i == 6:
        print("La condición del while es False, la variable i vale 6")
    
    print("Entramos al else del while")
    print("La condición del while es False")


print("Fin del programa")
