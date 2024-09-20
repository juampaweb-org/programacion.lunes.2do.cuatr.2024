

# Vamos a ver primero como en Python podemos hacer asignación doble de variables

# Asignación simple
a = 10

# Asignación doble
a = b = 10

# Asignación múltiple
a, b = 10, 20

# Con este ejemplo podemos dar vuelta una lista de numeros utilizando la asignación doble.

# Vemos un ejemplo con pocos numeros

listas_nros = [1, 2, 3, 4, 5]
print(listas_nros)

listas_nros[0], listas_nros[4] = listas_nros[4], listas_nros[0]
listas_nros[1], listas_nros[3] = listas_nros[3], listas_nros[1]
print(listas_nros)

# Vemos un ejemplo con muchos numeros

listas_nros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(listas_nros)


largo = len(listas_nros)
for i in range(largo//2):
    listas_nros[i], listas_nros[largo - i - 1] = listas_nros[largo - i - 1], listas_nros[i]

print(listas_nros)

# En este ejemplo vemos como podemos dar vuelta una lista de numeros utilizando la asignación doble.
# Lo que hacemos es intercambiar el primer elemento con el último, el segundo con el penúltimo, y así sucesivamente.


