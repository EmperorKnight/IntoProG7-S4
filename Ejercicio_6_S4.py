# Crea un algoritmo que dado el año de nacimiento de una persona y el año actual,
# calcule su edad actual y su edad en 10 años.

from datetime import date
from datetime import datetime

nacimiento = int(input(f"Introduzca su año de nacimiento \n-> "))

hoy = datetime.now()
edad_actual = 2025 - nacimiento
edad_futura = edad_actual + 10

print(f"Su edad es {edad_actual} \nSu edad dentro de 10 años es {edad_futura:.0f}")

# hoy = date.year()
# now = datetime.now()
# print(hoy)
# print(now)