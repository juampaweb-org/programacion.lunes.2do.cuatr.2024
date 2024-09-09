"""
10. Solicita al usuario que ingrese un número del 1 al 7.
Luego, imprime el día de la semana correspondiente(1 para Lunes,
2 para Martes, etc.). Si ingresa un número fuera de ese rango,
imprime "Número de día no válido".
"""
num = int(input("Ingrese un numero del 1 al 7: "))

match num:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Número de día no válido")
