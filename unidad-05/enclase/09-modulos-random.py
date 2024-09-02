

import random






print(" Vamos a imprimir diez números random entre 0 y 1")


for i in range(10):
    print(random.random() * 100)


############################################################


# seed() -> nos permite fijar una semilla para que los números random generados sean los mismos en cada ejecución del programa

random.seed(3)
print("Serie #1:", random.random(), random.random(), random.random())
random.seed(3)
print("Serie #2:", random.random(), random.random(), random.random())



############################################################



# número aleatorio, diferentes metodos

random.seed() # aplico esto por que antes habia seteado en 3 la semilla entonces siempre iban a ser los mismos nros aleatorios. acá reseteo la semilla

for i in range(10):
    print("Aleatorio del 1 al 10 -> ", random.randint(1, 10))
    print("Aleatorio del 20 al 30 -> ", random.randrange(20, 30))
    print('---------------------------')


############################################################





# choice() -> nos va a devolver un elemento random de la lista que le pasamos como argumento
# sample() -> nos va a devolver una lista con elementos random de la lista que le pasamos como primer argumento, el segundo argumento es la cantidad de elementos que queremos que nos devuelva

dado = [1, 2, 3, 4, 5, 6]
print("Dado: ", random.choice(dado))
print(random.sample(dado, 3))
# salida de terminal
# $ python3 mod_random.py
#
# Dado: 3
# [6, 5, 2]


