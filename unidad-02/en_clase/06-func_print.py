# Imprimir un mensaje simple
print("Hola mundo")


# Imprimir múltiples mensajes separados por un espacio por defecto, concatena strings en este caso
print("Hola", "a", "todos")

# Imprimir múltiples mensajes separados por un guion
print("Python", "es", "genial", sep="-")

# Imprimir usando el parámetro end para evitar un salto de línea
print("Hola", end=" ")
print("a", end=" ")
print("todos")

# Imprimir usando caracteres de escape para imprimir comillas dobles y simples
print("Ella dijo: \"Hola\"")
print('Él dijo: \'Hola\'')

# Imprimir una nueva línea usando el caracter de escape '\n'
print("Primera línea\nSegunda línea")

# Concatenar diferentes strings
mensaje1 = "Hola"
mensaje2 = "mundo"
print(mensaje1 + mensaje2)

# Imprimir utilizando todos los parámetros juntos
print("El resultado de la suma es:", 5 + 3, sep=" ", end="\n\n")
print("Adiós")
