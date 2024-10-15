

def si_es_blanco(calificacion):
    if calificacion > 7 :
        return "C"
    else:
         return "D"

def calificacion_estudiante(calificacion,nombre):

    if calificacion> 9 and calificacion<10:
      letra_calificacion="A"
    else:
        if calificacion>8 and calificacion<8.9:
           letra_calificacion="B"
        else:
            si_es_blanco(calificacion)
         

    return letra_calificacion
nota_alumno=7.5
nombre_alumno="Gabriel"
print("La calificacion de",nombre_alumno,"es: ",str(nota_alumno), ", su letra es:",calificacion_estudiante(nota_alumno,nombre_alumno))
