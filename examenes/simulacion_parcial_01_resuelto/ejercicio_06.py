"""
EJERCICIO 6
###########

Desarrolla un programa que convierta unidades de medida de distancia (kilómetros a millas) y peso (kilogramos a libras). El usuario debe seleccionar la conversión que desea realizar y el programa debe mostrar el resultado convertido.

Debe realizar todas las funciones por separado, y deben estar en un modulo aparte que se llame conversiones.
También debe utilizar docstrings para documentar las funciones.
https://peps.python.org/pep-0257/#one-line-docstrings 


El menú puede ser:

1. Convertir distancia, Kilómetros a Millas
2. Convertir peso, Kilogramos a Libras
3. Salir

"""

# Importar el módulo conversiones
import conversiones as conv


def main():
    imprimir_menu = True
    while imprimir_menu:
        print("\n\n\nMenú de opciones")
        print("################")
        print("1. Convertir distancia, Kilómetros a Millas")
        print("2. Convertir peso, Kilogramos a Libras")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            kilometros = float(input("Ingrese la cantidad de kilómetros: "))
            millas = conv.convertir_distancia(kilometros)
            print(f" -------->> {kilometros} kilómetros son {millas} millas.")
        elif opcion == "2":
            kilogramos = float(input("Ingrese la cantidad de kilogramos: "))
            libras = conv.convertir_peso(kilogramos)
            print(f" -------->> {kilogramos} kilogramos son {libras} libras.")
        elif opcion == "3":
            print("Saliendo del programa...")
            imprimir_menu = False
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()






