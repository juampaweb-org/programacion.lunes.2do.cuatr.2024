


# Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave y valor.

# Algunas propiedades de los diccionario en Python son las siguientes:

# Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
# Son indexados, los elementos del diccionario son accesibles a través del key.
# Y son anidados, un diccionario puede contener a otro diccionario en su campo value.


# Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value. En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.

diccionario_uno = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}


diccionario_vacio = dict()


#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

# También podemos utilizar la función dict() para crear un diccionario. En este caso, debemos pasar una lista de tuplas, donde cada tupla contiene la llave y el valor.

d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])

# exit()
#{'Nombre': 'Sara', 'Edad': '27', 'Documento': '1003882'}

# O le podemos indicar la clave directamente de la siguiente manera:

d3 = dict(
    Nombre='Sara',
    Edad=27,
    Documento=1003882,
    )
print(d3)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}


d3.insert(0, 'Apellido', 'Perez')

print(d3)