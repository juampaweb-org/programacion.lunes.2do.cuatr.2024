



subcadena_uno = "mi"
subcadena_dos = "la"
subcadena_tres = "ne"
subcadena_cuatro = "sas"

# concatenar
cadena_total = subcadena_uno + subcadena_dos + subcadena_tres + subcadena_cuatro

print(cadena_total)

#########################################################


# Uso de len()

longitud_cadena = len(cadena_total)
print(" La longitud de la cadena es: ", longitud_cadena)

#########################################################


# Uso de index() -> nos va a devolver el indice de la primera ocurrencia de la subcadena que le pasamos como argumento

cadena = "Python es un lenguaje de alto nivel"

indice = cadena.index("lenguaje")

print("El indice de la palabra 'lenguaje' es: ", indice)


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

print(cadena[:-1])
# salida: Python es un lenguaje de alto nive

print(cadena[-1])
# salida: l



#########################################################



# in y not in -> nos va a devolver True si la subcadena que le pasamos como argumento está en la cadena, False en caso contrario

cadena = "Python es un lenguaje de alto nivel"

if "lenguaje" in cadena:
    print("La subcadena 'lenguaje' está en la cadena")

if "lenguaje" not in cadena:
    print("La subcadena 'lenguaje' no está en la cadena")


