


alumno_nombre = "Patricio"
alumno_edad = 12
print( alumno_nombre + " tiene " + str(alumno_edad) + " años" )
print("-" * 80)

# Ahora vamos a utilizar match con condiciones
print("-" * 80)
print("Ahora vamos a utilizar match con condiciones y pipe")
print("-" * 80)

match alumno_edad:
    case 18 | 19 | 20:  # Caso 18, 19 o 20 años
        print(alumno_nombre + " tiene 18, 19 o 20 años")
        print("El alumno " + alumno_nombre + " es mayor de edad")
        print("Puede ingresar al bar")
    case 16 | 17:
        print(alumno_nombre + " tiene 16 o 17 años")
        print("El alumno " + alumno_nombre + " es menor de edad")
        print("Puede ingresar al bar con un mayor de edad")
    case 15:
        print(alumno_nombre + " tiene 15 años")
    case _:     # Caso por defecto
        print(alumno_nombre + " tiene " + str(alumno_edad) + " años")
        print("Entra al caso default")


print("Fin del programa")
