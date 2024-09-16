



subcadena_uno = "mi"
subcadena_dos = "la"
subcadena_tres = "ne"
subcadena_cuatro = "sas--------------------------"

# concatenar
cadena_total = subcadena_uno + subcadena_dos + subcadena_tres + subcadena_cuatro

# print(cadena_total)

#########################################################


# Uso de len()

longitud_cadena = len(cadena_total)
print(" La longitud de la cadena es: ", longitud_cadena)

print("el tipo de dato de la variable longitud_cadena es: ", type(longitud_cadena))

#########################################################


# Uso de index() -> nos va a devolver el indice de la primera ocurrencia de la subcadena que le pasamos como argumento

cadena = "Python es un lenguaje de alto nivel"

indice = cadena.index("e")

print("El indice del caracter 'e' es: ", indice)


#########################################################


# Vamos a probar las diferentes maneras de ver los indices de una cadena


cadena = "Python es un lenguaje de alto nivel"

print(cadena[0])
# salida: P

print(cadena[0:10])
# salida: Python es

print(cadena[10:20])
# salida: un lenguaj

print(cadena[0:20:2])
# salida: Pto su ega


print(cadena[:-2])
# salida: Python es un lenguaje de alto nive

print(cadena[-2])
# salida: l

#########################################################



# in y not in -> nos va a devolver True si la subcadena que le pasamos como argumento está en la cadena, False en caso contrario

cadena = "Python es un lenguaje de alto nivel"

if "pepe" in cadena:
    print("La subcadena 'pepe' está en la cadena")

if "pepe" not in cadena:
    print("La subcadena 'pepe' no está en la cadena")


