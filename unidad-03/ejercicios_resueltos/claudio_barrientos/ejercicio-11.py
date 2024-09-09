"""
11.Calculadora básica
Crea un programa que tome dos números como entrada y
luego imprima la suma, resta, multiplicación y
división de esos dos números.
Usa operadores aritméticos y
asegúrate de manejar casos donde el divisor sea cero.
"""

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un segundo número: "))
print("Suma: ", num1+num2)
print("Resta: ", num1-num2)
print("Multiplicación: ", num1*num2)
try:
    print("División: ", num1/num2)
except ZeroDivisionError:
    print("División: *El divisor ingresado es cero*")
