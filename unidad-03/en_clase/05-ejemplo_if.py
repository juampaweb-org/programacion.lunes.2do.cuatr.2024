







edad = int( input("Escribí tu edad: ") )


if edad >= 18:
    # acá empieza el bloque de codigo si la condicion es verdadera
    print("Sos mayor de edad")
    print("Podes votar")
    print("Podes manejar")
    print("Podes comprar alcohol")
    print("Podes ir a la carcel")
    # fin del bloque
else:
    # este es el principio del bloque de codigo si la condicion es falsa
    if edad >= 16:
        print("Sos menor de edad")
        print("Si estas en CABA podes sacar el registro")
        exit()
    else:
        numero = 2 + 2
    
    # sigue acá


print("Esto lo ejecuta en todos los casos.......")













# Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si
# la división es exacta o no.


numero_uno = int(input("Ingrese el primer numero: "))

numero_dos = int(input("Ingrese el segundo numero: "))

resultado = numero_uno % numero_dos

if resultado == 0:
    print("El resultado es exacto")
else:
    print("El resultado no es exacto, el resto es", resultado)



