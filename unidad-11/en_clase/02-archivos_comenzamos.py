


# Ruta absoluta
# C:\Users\Usuario\Documents\Python\unidad-11\en_clase\02-archivos_comenzamos.py


# Archivos en Windows
# Ruta absoluta
# C:\Users\Usuario\Documents\Python\unidad-11\en_clase\02-archivos_comenzamos.py


# Ruta relativa en LINUX
# en_clase/02-archivos_comenzamos.py

# Ruta Absoluta en LINUX
# /home/usuario/Documentos/Python/unidad-11/en_clase/02-archivos_comenzamos.py


directorio = '/var/www/html/istea/infra/programacion.lunes.2do.cuatr.2024/unidad-11/en_clase/'

nombre_archivo = 'archivo_unoppp.txt'
nombre_archivo_dos = 'archivo_pepe_dos.txt'
# ruta_completa = directorio + nombre_archivo


try:
    ruta_completa = directorio + nombre_archivo
    archivo = open( ruta_completa, 'r')
    print("El archivo se abrió correctamente....")
    
    
    linea = archivo.readline()

    while linea != '':
        print(linea)
        linea = archivo.readline()
    
    
    archivo.close()
    print("El archivo se cerró correctamente....")

except IOError as e:
    print("Errorr: ", e)




print("Fin del programa......")


