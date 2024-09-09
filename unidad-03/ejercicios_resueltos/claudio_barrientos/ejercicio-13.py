"""
13.Conversión de unidades
Escribe un programa que convierta una temperatura dada
en grados Celsius a grados Fahrenheit.
La fórmula de conversión es `F = C * 9/5 + 32`.
Pide al usuario que ingrese una temperatura en Celsius
y muestra el resultado en Fahrenheit.
"""
temp = float(input("Ingrese la temperatura en Celsius: "))

print("Temperatura en Farenheit: ", (temp*9/5+32))
