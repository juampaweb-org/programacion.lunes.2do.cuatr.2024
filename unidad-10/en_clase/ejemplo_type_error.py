


nombres = ["Juan", "Pedro", "María"]

try:
    print(nombres[1.34])
except TypeError:
    print("El índice debe ser un número entero")
except:
    print("Error desconocido")

print("Fin del programa")


