

# Accediendo a los diccionarios

telefono_sara = {
    'celular': 123456789,
    'fijo': 3232323
}
nros_de_telefono = {
    "Sara": 87687687,
    "Juan": 987654321,
    "Pedro": 456789123,
    "Pepe": 278227222,
    "Lucia": 123456789,
}


nros_de_telefono["Lucia"] = 987654321345345

print(nros_de_telefono)

exit()



print(nros_de_telefono.items())


for clave, valor in nros_de_telefono.items():
    print("Clave: ", clave)
    print("Valor: ", valor)

exit()




# print(nros_de_telefono.keys())  # dict_keys(['Sara', 'Juan', 'Pedro'])
for num in nros_de_telefono.items():
    print("Valor: ", num)





exit()


if "Sara" in nros_de_telefono:
    print("el valor existe")  # 123456789


exit()



# Y podemos usar in i not in para saber si existe la clave en el diccionario por que si no existe nos va a dar un error.

if "Sara" in nros_de_telefono:
    print("Sara existe en el diccionario")
else:
    print("Sara no existe en el diccionario")

exit()


if "Carlos" not in nros_de_telefono:
    print("Carlos no existe en el diccionario")


