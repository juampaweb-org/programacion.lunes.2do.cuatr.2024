"""
14.Juego de adivinanza
Crea un programa que pida al usuario que adivine un número entre 1 y 10.
El programa debe comparar el número ingresado con uno predefinido
(por ejemplo, 7) y decir si es correcto o no. Si es incorrecto,
debe dar una pista si el número es mayor o menor.
"""
import random

num2 = random.randint(1, 10)
print("Adiviná el numero!")
num = int(input("Ingrese un numero del 1 al 10: "))

while num != num2:
    if num > num2:
        print("Incorrecto!\nPista: es un número menor")
    elif num < num2:
        print("Incorrecto!\nPista: es un número mayor")
    num = int(input("Volvé a ingresar un numero del 1 al 10: "))
print("Adivinaste!!")
