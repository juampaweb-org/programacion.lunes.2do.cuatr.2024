

archivo = 'temperaturas.txt'

try:

    with open(archivo, 'r') as stream_archivo:
        archivo_completo = stream_archivo.readlines()
        
        for linea in archivo_completo:
            if linea == '2023-02-17,51,44\n':
                print("Encontré la línea que buscaba.....")
                break

    # aca me lo cierra solo

    # stream_archivo.close()

except:
    print("Por algún motivo, no se pudo abrir el archivo....")



