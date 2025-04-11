# Calcula la calificación final de un estudiante con ponderaciones:
# Tareas: 30%
# Examen parcial: 30%
# Examen final: 40%

iniciador = 0

cantidad_tareas = int(input(f" \nIntroduzca la cantidad de tareas que califico \n-> "))
calificacion_tareas = float(input(f"Introduzca la calificacion que saco el estudiante en las tares \n-> "))

for iniciador in range(1,cantidad_tareas):
    calificacion_tareas1 = float(input("-> "))
    calificacion_tareas = calificacion_tareas + calificacion_tareas1

examen_parcial = float(input(f"Introduzca la calificacion del estudiante en el examen parcial (max 30)\n-> "))
examen_final = float(input(f"Introduzca la calificacion del estudiante en el examen final (max 40) \n-> "))

calificacion_final = calificacion_tareas + examen_parcial + examen_final

print(f" \nLa calificacion del estudiante en las tareas es de {calificacion_tareas:.0f}/30")
print(f"La calificacion del estudiante en el examen parcial es de {examen_parcial:.0f}/30")
print(f"La calificacion del estudiante en el examen final es de {examen_final:.0f}/40")
print(f"La calificacion final del estudiante es de {calificacion_final:.0f}/100\n ")


