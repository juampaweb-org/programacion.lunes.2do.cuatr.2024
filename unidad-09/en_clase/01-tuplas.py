

# Las tuplas en Python son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables.

# Creación de una tupla

# Para crear una tupla en Python, se utilizan paréntesis en lugar de corchetes. Por ejemplo:
tupla = (1, 2, 3, 4, 5)


# Si queremos crear una tupla vacía, simplemente escribimos los paréntesis sin ningún elemento dentro:
tupla_vacia = ()

# Si queremos crear una tupla con un solo elemento, debemos agregar una coma al final del elemento:
tupla_un_elemento = (1,)


# Acceder a los elementos de una tupla
tupla_nombres = ('Juan', 'Pedro', 'María', 'Ana', 'Lucía', 'Paz', 'Angela')

# Recorrido de los elementos de una tupla
for nombre in tupla_nombres:
    print(nombre)

# Imprimimos el largo de la tupla
print(len(tupla_nombres))  # 5

# Accedemos al indice 2
print(tupla_nombres[2])  # María

# Y tenemos la posibilidad de ir accediendo de manera inversa
print(tupla_nombres[-1])  # Lucía

# También recorrer de dos en dos
for nombre in tupla_nombres[::2]:
    print(nombre)

# IMPORTANTE! No podemos modificar los elementos de una tupla, si intentamos hacerlo obtendremos un error:

# tupla_nombres[0] = 'Carlos'  # TypeError: 'tuple' object does not support item assignment

# Tampoco tiene el metodo append()

tupla_nombres.append('Carlos')  # AttributeError: 'tuple' object has no attribute 'append'

exit()

# Tenemos dos metodos en las tuplas

# count() - Devuelve el número de veces que aparece un valor en la tupla
# index() - Devuelve el índice en el que aparece un valor en la tupla

# ejemplos

tupla_numeros = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

print(tupla_numeros.count(1))  # 2

print(tupla_numeros.index(3))  # 2



