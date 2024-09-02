


## pass -> No hace nada, continua a la siguiente instrucción
for i in range(10):
    print("La variable i vale: ", i)
    pass
    print("Aca sigue....")

#####################################################



## otro ejemplo, con if. Si no ponemos el pass, da error de sintaxis

if (i == 0):
    print("i es cero")
else: 
    pass

#####################################################


# Uso de break -> me saca del bloque de for
for i in range(10):
    # Inicio del bloque de for
    print(i)
    if i == 7:
        break # me saca afuera del for
    # Fin del bloque de for

#####################################################



nombres = ["Juan", "Pedro", "María", "Ana", "Luis", "Carlos"]

# Uso de continue -> salta a la siguiente iteración, es decir vuelve arriba del for y obliga a la siguiente iteración
for nombre in nombres:
    if nombre != "Ana":
        continue
    print("Esto se imprime si el nombre es Ana")
    print("aca sigue el for..")
    break

print("Acá ya estamos afuera del for()")
print("Fin del programa---")


#####################################################

    