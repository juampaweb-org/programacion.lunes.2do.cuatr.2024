"""
12.Calculador de IMC
Crea un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
Pide al usuario su peso en kilogramos y su altura en metros.
Luego, calcula el IMC usando la fórmula `IMC = peso / altura**2` y
muestra el resultado con un mensaje que indique
si el IMC está en el rango normal, bajo peso, sobrepeso, etc.

IMC menor 18 = PESO BAJO
IMC entre 18 y 24 = PESO NORMAL
IMC entre 25 y 29 = SOBREPESO
IMC entre 30 y 34 = OBESIDAD
IMC entre 35 y 40 = OBESIDAD SEVERA
IMC mayor de 40 = OBESIDAD MORBIDA
"""
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / altura ** 2

match imc:
    case _ if imc < 18:
        print("IMC = ", imc, "\nPESO BAJO")
    case _ if imc >= 18 and imc <= 24:
        print("IMC = ", imc, "\nPESO NORMAL")
    case _ if imc >= 25 and imc <= 29:
        print("IMC = ", imc, "\nSOBREPESO")
    case _ if imc >= 30 and imc <= 34:
        print("IMC = ", imc, "\nOBESIDAD")
    case _ if imc >= 35 and imc <= 40:
        print("IMC = ", imc, "\nOBESIDAD SEVERA")
    case _ if imc > 40:
        print("IMC = ", imc, "\nOBESIDAD SEVERA")
