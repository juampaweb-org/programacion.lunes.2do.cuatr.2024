

# Accediendo a los diccionarios

nros_de_telefono = {
    "Sara": 123456789,
    "Juan": 987654321,
    "Pedro": 456789123
}

print(nros_de_telefono["Sara"])  # 123456789

# Y podemos usar in i not in para saber si existe la clave en el diccionario por que si no existe nos va a dar un error.

if "Sara" in nros_de_telefono:
    print("Sara existe en el diccionario")

if "Carlos" not in nros_de_telefono:
    print("Carlos no existe en el diccionario")


