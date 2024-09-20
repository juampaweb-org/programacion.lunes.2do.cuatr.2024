
# voy a guardar en 0 el nombre y en 1 el apellido
datos = [ False, False, False ]


nombre = input("Ingrese su nombre: ")
datos[0] = nombre

apellido = input("Ingrese su apellido: ")
datos[1] = apellido

edad = input("Ingrese su edad: ")
datos[2] = edad

for dato in datos:
    print(dato)

exit()




# Una lista es un tipo de datos que permite almacenar varios valores en una sola variable.


# Algunas características de las listas son:

# Son ordenadas, mantienen el orden en el que han sido definidas
# Pueden ser formadas por tipos arbitrarios
# Pueden ser indexadas con [i].
# Se pueden anidar, es decir, meter una dentro de la otra.
# Son mutables, ya que sus elementos pueden ser modificados.
# Son dinámicas, ya que se pueden añadir o eliminar elementos.


lista_de_numeros = [12, 37, 5, 42, 8, 3]

# Acceder a un elemento de la lista
print("Lista de numeros sin haber sido modificada...")
print(lista_de_numeros)  # 12

# Modificar un elemento de la lista
lista_de_numeros[0] = 100
print("Lista de numeros después de haber sido modificada...")
print(lista_de_numeros)



# Agregar un elemento al final de la lista
lista_de_numeros.append(1024)

print(lista_de_numeros)



# Agregar un elemento en una posición específica
lista_de_numeros.insert(0, 879)
lista_de_numeros.insert(2, 100)
lista_de_numeros.insert(4, "Pedro")
print(lista_de_numeros)


# Eliminar un elemento de la lista
lista_de_numeros.remove(100)
# lista_de_numeros.remove(100)
lista_de_numeros.remove("Pedro")


# Eliminar un elemento de la lista por su índice
del lista_de_numeros[4]


print(lista_de_numeros)

# Eliminar el último elemento de la lista
lista_de_numeros.pop()
lista_de_numeros.pop()
lista_de_numeros.pop()

print(lista_de_numeros)

# Obtener la longitud de la lista
print("La cantidad de elementos que tiene la lista:")
print(len(lista_de_numeros))



# Iterar sobre los elementos de la lista
lista_de_numeros = [2, 5, 3, "Juan", 40, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

lista_de_numeros_original = lista_de_numeros

numero = lista_de_numeros[0:2]
for num in numero:
    print(type(num))

exit()

print(lista_de_numeros_original)
print(lista_de_numeros)


exit()


for nombre in nombres:
    print(nombre)



# Crear una lista vacía
lista_vacia = []





