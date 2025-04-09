# Crea un algoritmo que dado el año de nacimiento de una persona y el año actual,
# calcule su edad actual y su edad en 10 años.

nacimiento = int(input(f"Introduzca su año de nacimiento \n-> "))

edad_actual = 2025 - nacimiento
edad_futura = edad_actual + 10

print(f"Su edad actual es de {edad_actual}. \nSu edad dentro de 10 años es {edad_futura:.0f}.")
