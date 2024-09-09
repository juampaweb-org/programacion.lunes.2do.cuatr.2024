"""
16.Calculador de calificaciones
Crea un programa que pida al usuario que ingrese sus calificaciones
en tres materias. Luego, calcula el promedio de esas calificaciones
e imprime un mensaje que indique si el alumno aprobó (promedio ≥ 6) o no.
"""
nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = (nota1+nota2+nota3)/3

if promedio >= 6:
    print("Aprobó: ", promedio)
else:
    print("No aprobó: ", promedio)
