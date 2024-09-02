# Vamos a usar while

# Ejemplo básico de estructura while:
# while condicion:
#     intrucciones 1
#     intrucciones 2
#     intrucciones 3
#     ...

numero = 0

while (numero < 11):
    
    if numero % 2 == 0:
        print("el número " + str(numero) + " es par")
    else:
        print("el número " + str(numero) + " es impar")
    
    numero += 1


print("Acá ya salio del bloque while")

exit()



# Definición de una variable de tipo string
color = "rojo"

# Tipos de datos booleanos: True o False
variable_uno = True

# Ejemplo de uso de while con una condición booleana
while variable_uno == True:
    # Este bloque de código se ejecuta una sola vez
    print("Acá va a entrar una sola vez.....")
    # Cambiamos el valor de variable_uno a un tipo diferente (string en este caso)
    variable_uno = "cualquier texto"

# Mensaje de fin del programa una vez que el bucle while termina
print("Fin del programa")

# Ejemplo de uso de while con una condición basada en el valor de una variable
while color == "rojo":
    # Este bloque de código se ejecuta repetidamente mientras color sea "rojo"
    print("El color es rojo")
    print("Sigo en el while......")
    print("Sigo en el while......")
    print("Ahora voy a volver a preguntar por la condición del while")
    # Cambiamos el valor de color para salir del bucle
    color = "verde"

# Mensaje de fin del programa una vez que el bucle while termina
print("Fin del programa")








#### Otro programa con while ####

# Inicializamos nuestra variable de control
numero = 1

# Comenzamos el bucle while
while numero <= 5:
    print(numero)  # Imprimimos el número actual
    numero += 1    # Incrementamos el número en 1 para la siguiente iteración








#### Otro programa con while ####


# Bucle infinito utilizando while

# Descomentar para ejecutar

"""
nombre = "Analia"

while nombre == "Analia":
    print("Hola Analia!")
    print("Este es un bucle infinito. Presiona Ctrl+C para detenerlo.")

"""







