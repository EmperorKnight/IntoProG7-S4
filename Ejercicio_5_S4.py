# Algoritmo que calcule el porcentaje de un número dado. Ejemplo: ¿qué es el 15% de 200?

numero_porcentado = int(input(f"Introduzca un numero \n-> "))
numero_porcentaje = int(input(f"Introduzca el porcentaje que quiere conocer del numero que introdujo \n-> "))

Total = numero_porcentaje / 100
Total *= numero_porcentado

print(f"El porcentaje de {numero_porcentado} por el {numero_porcentaje} es {Total:.0f}")

