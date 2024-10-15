# Tupla de colores
colores_favoritos = ("naranja", "verde", "negro")

# Comprobando si un color es favorito
color_a_verificar = "verde"

if color_a_verificar in colores_favoritos:
    print(f"{color_a_verificar.capitalize()} es uno de mis colores favoritos.")

# Verificando un color que no es favorito
color_no_favorito = "azul"

if color_no_favorito not in colores_favoritos:
    print(f"{color_no_favorito.capitalize()} no es uno de mis colores favoritos.")



datos_personales = {
    "Nombre": "Sara",
    "Edad": 27,
    "Documento": 27654555
}

print("Valores del diccionario: ", datos_personales.values())

