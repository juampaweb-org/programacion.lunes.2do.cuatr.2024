

counter = 0

stream = open("archivo_uno.txt", "rt", encoding="utf-8")

caracter = stream.read(1)
while caracter != "":
    print(caracter, end="")
    counter += 1
    caracter = stream.read(1)

stream.close()
print(f"\n\nSe leyeron {counter} caracteres.")

