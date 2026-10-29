notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
#indica cuantos alumnos han aprobado
aprobados=0
for n in notas_alumnos:
    if n>=5:
        aprobados=aprobados+1
print("El total de aprobados es ",aprobados)
#indica la nota más alta
"""
mayor=notas_alumnos[0] #inicializamos la variable con cualquiera de las notas
for nota in notas_alumnos:
    if nota>mayor:
        mayor=nota
print(f"La nota más alta es {mayor}")
"""
print(f"La nota más alta es {max(notas_alumnos)}")
print(f"La nota más baja es {min(notas_alumnos)}")
print(f"Las notas en orden son: {sorted(notas_alumnos,reverse=True)}")
