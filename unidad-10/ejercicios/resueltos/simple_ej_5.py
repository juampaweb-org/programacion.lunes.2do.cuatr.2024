# 5. Operación matemática inválida:
# Solicita al usuario una operación matemática (+, -, *, /) y dos números. Realiza la operación solicitada, manejando el error si la operación ingresada no es válida.


operacion = input("Ingrese la operación matemática (+, -, *, /): ")

if operacion not in ["+", "-", "*", "/"]:
    print("Operación inválida")
    exit()

numero_uno = input("Ingrese el primer número: ")
numero_dos = input("Ingrese el segundo número: ")

if not numero_uno.isdigit() or not numero_dos.isdigit():
    print("Los números ingresados no son válidos")
    exit()

if operacion == "+":
    resultado = int(numero_uno) + int(numero_dos)

elif operacion == "-":
    resultado = int(numero_uno) - int(numero_dos)

elif operacion == "*":
    resultado = int(numero_uno) * int(numero_dos)

elif operacion == "/":
    try:
        resultado = int(numero_uno) / int(numero_dos)
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        exit()

print(f"El resultado de la operación es: {resultado}")
