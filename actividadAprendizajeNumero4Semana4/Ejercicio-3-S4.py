# Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su
# salario actual y un descuento de 2,5% por servicios.

print(" ")
salario_actual = float(input(f"Introduzca el salario actual del empleado \n-> "))

incremento = (8/100) * salario_actual
descuento_por_servicios = (2.5/100)
nuevo_salario = (salario_actual + incremento) * descuento_por_servicios

print(" ")
print(f"El nuevo salario del empleado es de C${nuevo_salario:,.2f}")
print(" ")

 