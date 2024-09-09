"""
8. Pide al usuario que ingrese una temperatura en Celsius.
Si la temperatura es mayor o igual a 100, imprime "El agua está hirviendo".
Si es menor o igual a 0, imprime "El agua está congelada".
De lo contrario, imprime "El agua está en estado líquido".
"""
temp = float(input("Ingrese una temperatura: "))

if temp >= 100:
    print("El agua está hirviendo")
else:
    if temp <= 0:
        print("El agua está congelada")
    else:
        print("El agua está en estado líquido")
