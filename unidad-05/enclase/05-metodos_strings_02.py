



# count() -> nos va a devolver la cantidad de veces que aparece la subcadena que le pasamos como argumento

cadena = "Python es un lenguaje de alto nivel"

cantidad = cadena.count("e")

print("La cantidad de veces que aparece la letra 'e' es: ", cantidad)

########################################################



# isdigit() -> nos va a devolver True si la cadena es un número, False en caso contrario

cadena = "1234"

if cadena.isdigit():
    print("La cadena es un número")
else:
    print("La cadena no es un número")


########################################################



# upper() -> nos va a devolver la cadena en mayúsculas

cadena = "Python es un lenguaje de alto nivel"

cadena_mayusculas = cadena.upper()

print(cadena_mayusculas)


########################################################


# lower() -> nos va a devolver la cadena en minúsculas

cadena = "Python es un lenguaje de alto nivel"

cadena_minusculas = cadena.lower()

print(cadena_minusculas)


########################################################




# ljust() -> nos va a devolver la cadena justificada a la izquierda con el caracter que le pasamos como argumento

cadena = "Python es un lenguaje de alto nivel"

cadena_izq = cadena.ljust(50, "*")

print(cadena_izq)


########################################################


# rjust() -> nos va a devolver la cadena justificada a la derecha con el caracter que le pasamos como argumento

cadena = "Python es un lenguaje de alto nivel"

cadena_der = cadena.rjust(50, "*")

print(cadena_der)


########################################################


# replace() -> nos va a devolver la cadena reemplazando la subcadena que le pasamos como primer argumento por la subcadena que le pasamos como segundo argumento

cadena = "Python es un lenguaje de alto nivel"

cadena_reemplazada = cadena.replace("Python", "Java")

print(cadena_reemplazada)

