



def calificacion_estudiante(calificacion,nombre):

    if calificacion> 9 and calificacion<10:
      letra_calificacion="A"
    else:
        if calificacion>8 and calificacion<8.9:
           letra_calificacion="B"
        else:
            if calificacion>7 and calificacion<7.9:
               letra_calificacion="C"
            else:
                if calificacion>6 and calificacion<6.9:
                   letra_calificacion="D"
                else:
                   letra_calificacion="F"
    return letra_calificacion
nota_alumno=7.5
nombre_alumno="Gabriel"
print("La calificacion de",nombre_alumno,"es: ",str(nota_alumno), ", su letra es:",calificacion_estudiante(nota_alumno,nombre_alumno))
