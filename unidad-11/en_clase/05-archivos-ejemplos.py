



# Leer el archivo de telefonos e ir guardando todos los telefonos en una lista.
# Luego mostrar la lista de telefonos.


directorio =  '/var/www/html/istea/infra/programacion-lunes.1er.cuatrimestre.2024/archivos/'

nombre_archivo = 'telefonos.txt'

telefonos = []


archivo = open(directorio + nombre_archivo, 'r')

print("Agregando telefonos a la lista......")

for linea in archivo.readlines():
    telefonos.append(linea)

print("Telefonos agregados correctamente.")

print("Mostramos la lista:")
print(telefonos)

print("Accedemos a un telefono especifico:")
print(telefonos[11])

print("Vamos a recorrer la lista")



for indice in range(len(telefonos)):
    print(telefonos[indice])
    
    














archivo.close()






