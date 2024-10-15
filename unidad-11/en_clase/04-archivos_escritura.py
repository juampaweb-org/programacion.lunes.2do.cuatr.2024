



directorio =  '/var/www/html/istea/infra/programacion-lunes.1er.cuatrimestre.2024/archivos/'

nombre_archivo = 'telefonos.txt'

nombre_completo = directorio + nombre_archivo

archivo_escribir = open(nombre_completo, 'w')




for i in range(200):
    archivo_escribir.write(f"0{i}-1234-5678\n")