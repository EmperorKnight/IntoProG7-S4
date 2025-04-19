# Algoritmo que calcule el salario de un trabajador de la manera siguiente. El trabajador
# cobra un precio fijo por hora y se le descuento el 5% en concepto de impuesto sobre la
# renta. El programa debe pedir el nombre del trabajador, las horas trabajadas y el precio
# que cobra por hora. Como salida debe imprimir el nombre del trabajador, el sueldo bruto,
# el descuento de renta y el salario a paga.

Imp_renta = "5%"

nombre_trabajador = str(input(f" \nIntroduzca el nombre del trabajador \n-> "))
tiempo_trabajado = int(input(f"Introduzca el tiempo que trabajo en horas \n-> "))
precio_hora = float(input(f"Introduzca el precio que cobra el trabajador por hora \n-> "))

salario_pagar = precio_hora * tiempo_trabajado - (precio_hora * (5/100))

print(f" \nNombre: {nombre_trabajador} \nSueldo bruto: C${precio_hora} \nDescuento impuesto sobre la renta: {Imp_renta}")
print(f"Salario a pagar: C${salario_pagar} \n ")