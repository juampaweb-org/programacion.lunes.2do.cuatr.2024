

# Errores

# Errores de sintaxis

# Los errores de sintaxis son errores que se producen cuando el código no sigue las reglas de sintaxis del lenguaje de programación. Por ejemplo, si olvidamos cerrar una comilla o un paréntesis, o si escribimos una palabra clave incorrectamente, Python nos mostrará un mensaje de error de sintaxis.


print("pepe")
print("continuamos con el código....")
print("Hola, Mundo!)


# Errores semanticos o logicos.. los mas dificiles de encontrar

edad = int(input("Introduce tu edad: "))


if edad > 18: # Hay un error en el signo
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")




# Errores de tiempo de ejecución

# Los errores de tiempo de ejecución son errores que se producen durante la ejecución del programa. Estos errores pueden ser causados por una variedad de razones, como la entrada incorrecta del usuario, la falta de memoria, o la división por cero. Python mostrará un mensaje de error cuando se produzca un error de tiempo de ejecución.

numero = input("Ingresa un número: ")

try:
    numero = float(numero)
    print(f'el reciproco de {numero} es {1/numero}')

except ValueError:
    print("ERROR: El valor ingresado no es un número....")
    exit()

except ZeroDivisionError:
    print("ERROR: No se puede dividir por cero --------")

except as e:
    print("ERROR: Algo salió mal....", e)



print("Acá continua el programa.....")




try:

    numero = input("Ingresa un número: ")
    numero = float(numero)
    print("El reciproco de", numero, "es", 1/numero)


except ZeroDivisionError:
    print("No se puede dividir entre cero")

# except ValueError:
#     print("El valor ingresado no es un número")

# except TypeError:
#     print("El valor ingresado no es un número")


    








# try y except

# En Python, podemos manejar los errores de tiempo de ejecución utilizando la declaración try y except. La declaración try nos permite ejecutar un bloque de código y capturar cualquier excepción que se produzca. La declaración except nos permite manejar la excepción y tomar medidas para corregir el error.

