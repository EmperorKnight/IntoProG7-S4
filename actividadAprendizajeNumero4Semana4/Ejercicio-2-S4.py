# Algoritmo para calcular el porcentaje de mujeres y varones en un aula.

print(" ")
varones = int(input(f"Introduzca la cantidad total de estudiantes varones del aula \n-> "))
mujeres = int(input(f"Introduzca la cantidad total de estudiantes femeninas del aula \n-> "))

total = varones + mujeres
porcentaje_varones = (varones / total) * 100
porcentaje_mujeres = (mujeres / total) * 100 

print(" ")
print(f"El pocentaje de estudiantes varones presentes en el aula es de {porcentaje_varones}%")
print(f"El pocentaje de estudiantes femeninas presentes en el aula es de {porcentaje_mujeres}%")
print(" ")
