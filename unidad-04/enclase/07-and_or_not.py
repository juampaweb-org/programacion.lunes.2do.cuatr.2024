
### and ###

numero = 10

if numero == 8 or numero == 9 or numero == 10:
    print("El numero esta entre 8 y 10.")
elif numero == 11 or numero == 12 or numero == 13:
    print("El numero esta entre 11 y 13.")

exit()


if numero > 10 and numero < 20:
    print("El número está entre 10 y 20.")
else:
    print("El número está fuera del rango de 10 a 20.")

exit()

### or ###

numero = 120

if numero < 0 or numero > 100:
    print("El número es negativo o mayor que 100.")
else:
    print("El número está entre 0 y 100.")

### not ###

numero = 5

if not numero == 0:
    print("El número no es igual a cero.")
else:
    print("El número es igual a cero.")
