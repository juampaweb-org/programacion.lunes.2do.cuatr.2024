

# Trabajando con las listas

# metodo sort()

autos = ['Ford', 'BMW', 'Volvo']
print (autos)

# Ahora ordeno el objeto lista
autos.sort()
print (autos)



# por otro lado en vez del método tenemos a la función sorted()

autos = ['Ford', 'BMW', 'Volvo']

# Imprimo la lista ordenada, pero no la modifico
print (sorted(autos))

# Si vuelvo a imprimir la original no va a estar ordenada
print (autos)




# Crear una lista con un rango de números
lista_de_numeros = list(range(10))

# Crear una lista con un rango de números con un paso específico
lista_de_numeros = list(range(0, 10, 2))

# Crear una lista con una secuencia de caracteres
lista_de_caracteres = list("Hola mundo")
print(lista_de_caracteres)




# min() y max() y sum()

lista_de_numeros = [12, 37, 5, 42, 8, 3]

# Obtener el número más pequeño de la lista
print(min(lista_de_numeros))  # 3

# Obtener el número más grande de la lista
print(max(lista_de_numeros))  # 42

# Obtener la suma de todos los números de la lista
print(sum(lista_de_numeros))  # 107


