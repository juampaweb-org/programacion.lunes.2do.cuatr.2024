




# metodo para escribir archivos


try:
    archivo = open('telefonos.txt', 'w') # 'w' es para write, para escribir en el archivo
    # archivo = open('telefonos.txt', 'a') # 'a' es para append, para agregar al final del archivo

    # Escribir en el archivo un telefono de Argentina
    for digito in range(400):
        archivo.write(f'0{digito}-1234-5678\n')

    # cerrar el archivo
    archivo.close()

except Exception as error:
    print('Error al escribir el archivo: ', error)


print("Acá sigue el programa y finaliza.")


exit()

































directorio =  '/var/www/html/istea/infra/programacion-lunes.1er.cuatrimestre.2024/archivos/'

nombre_archivo = 'telefonos.txt'

nombre_completo = directorio + nombre_archivo

archivo_escribir = open(nombre_completo, 'w')




for i in range(200):
    archivo_escribir.write(f"0{i}-1234-5678\n")