



# Sentencias if

# La sentencia if permite ejecutar un bloque de código si una condición es verdadera.

alumno_nombre = "Federico"
alumno_edad = int(input("Ingrese la edad del alumno: "))


# Anidamientos de if / else

if alumno_edad > 40:
    mens_salida = "El alumno es mayor a 40 años"

elif alumno_edad > 30:
    mens_salida = "El alumno es mayor a 30 años"

elif alumno_edad > 20:
    mens_salida = "El alumno es mayor a 20 años"

else:
    mens_salida = "El alumno es menor a 20 años"


print(mens_salida)


print("fin del programa")
print("sigo acá....")