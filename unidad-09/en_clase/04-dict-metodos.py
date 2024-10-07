


# Metodo keys()

# El método keys() devuelve una vista de las llaves del diccionario, es decir, una lista con las llaves del diccionario.

agenda = {
    "Juan": 123456,
    "Pedro": 654321,
    "María": 987654
}

print(agenda.keys())  # dict_keys(['Juan', 'Pedro', 'María'])

# recorro las llaves del diccionario

for k in agenda.keys():
    print(k)


# Metodo values()

# El método values() devuelve una vista de los valores del diccionario, es decir, una lista con los valores del diccionario.

print(agenda.values())  # dict_values([123456, 654321, 987654])

# recorro los valores del diccionario

for valor in agenda.values():
    print(valor)


# Metodo items()

# El método items() devuelve una vista de los pares llave-valor del diccionario, es decir, una lista con los pares llave-valor del diccionario.

print(agenda.items())  # dict_items([('Juan', 123456), ('Pedro', 654321), ('María', 987654)])

# recorro los pares llave-valor del diccionario

for clave, valor in agenda.items():
    print(clave, valor)





