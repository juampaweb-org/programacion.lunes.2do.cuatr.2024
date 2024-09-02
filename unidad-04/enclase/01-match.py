



# Definición de variables
alumno_nombre = "Patricio"
alumno_edad = 15

# Mostrar el nombre del alumno junto con su edad en forma de texto / Concatenación de cadenas
print( alumno_nombre + " tiene " + str(alumno_edad) + " años" )

# Imprimir una línea separadora
print("-" * 80)


match alumno_edad:
    case 18:
        # un nuevo bloque de codigo
        print(alumno_nombre + " tiene 18 años")
        print("El alumno " + alumno_nombre + " es mayor de edad")
        print("Puede ingresar al bar")
        # aca termina el bloque de codigo si vale igual a 18
    case 17:
        print(alumno_nombre + " tiene 17 años")
        print("El alumno " + alumno_nombre + " es menor de edad, tiene 17 años")
        print("Puede ingresar al bar con un mayor de edad")
    case 16:
        print(alumno_nombre + " tiene 16 años")
        print("El alumno " + alumno_nombre + " es menor de edad, tiene 16 años")
        print("No puede ingresar al bar")
    case _:
        print("Entra caso default!!!!!-------------------")



exit()



# Uso de la estructura match (nueva en Python 3.10) para evaluar la edad del alumno
# match alumno_edad:
#     case 18:    # Caso 18 años
#         print(alumno_nombre + " tiene 18 años")
#         print("El alumno " + alumno_nombre + " es mayor de edad")
#         print("Puede ingresar al bar")
#     case 17:    # Caso 17 años
#         print(alumno_nombre + " tiene 17 años")
#         print("El alumno " + alumno_nombre + " es menor de edad, tiene 17 años")
#         print("Puede ingresar al bar con un mayor de edad")
#         print("Puede ingresar al bar con un mayor de edad")
#     case 16:    # Caso 16 años
#         print(alumno_nombre + " tiene 16 años")


# Otra forma de usar match con expresiones condicionales
match alumno_edad:
    # Caso si la edad es exactamente 18 años
    case _ if alumno_edad == 18:
        print(alumno_nombre + " tiene " + str(alumno_edad) + " años")
        print("El alumno " + alumno_nombre + " es mayor de edad")
        print("Puede ingresar al bar")
    # Caso si la edad es mayor que 18 años
    case _ if alumno_edad > 18:
        print(alumno_nombre + " tiene " + str(alumno_edad) + " años, es mayor que 18 años")
        print("El alumno " + alumno_nombre + " es mayor de edad")
        print("Puede ingresar al bar")
    # Caso si la edad es mayor o igual a 12 años
    case _ if alumno_edad >= 12:
        print(alumno_nombre + " tiene " + str(alumno_edad) + " años")
        print("El alumno " + alumno_nombre + " es menor de edad")
        print("Puede ingresar al bar con un mayor de edad")
    # Caso por defecto (edad menor a 12 años)
    case _:
        print(alumno_nombre + " tiene " + str(alumno_edad) + " años")
        print("El alumno " + alumno_nombre + " es menor de 12 años")
        print("No puede ingresar al bar")
