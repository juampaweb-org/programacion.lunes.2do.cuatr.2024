# 5. Pregunta al usuario que ingrese un número. 
# Si el número es mayor que 10, imprime "El número es mayor que 10". 
# Si es igual a 10, imprime "El número es igual a 10". 
# De lo contrario, imprime "El número es menor que 10".
# b. Solicita al usuario que ingrese dos números y compara si son iguales. 
# Si lo son, imprime "Los números son iguales". De lo contrario, imprime "Los números son diferentes".

numero = int(input("Ingrese un numero: "))

if numero > 10:
    print("El numero es mayor a 10.")
elif numero == 0:
    print("El numero es igual a 0.")
else:
    print ("El numero es menor a 10.")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))


if numero1 == numero2:
    print("Los numeros son iguales.")
else:
    print("Los numeros son diferentes.")

