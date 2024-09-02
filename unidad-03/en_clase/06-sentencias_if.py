



# Sentencias if

# La sentencia if permite ejecutar un bloque de código si una condición es verdadera.

alumno_nombre = "Federico"
alumno_edad = int(input("Ingrese la edad del alumno: "))


# Anidamientos de if / else
if alumno_edad > 40:
    print("El alumno", alumno_nombre, "es mayor de 40 años.")
else:
    if alumno_edad > 30:
        print("El alumno", alumno_nombre, "es mayor de 30 años.")
    else:
        print("El alumno", alumno_nombre, "es menor de 30 años.")

print("fin del programa")
print("sigo acá....")