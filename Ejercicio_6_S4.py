# Crea un algoritmo que dado el año de nacimiento de una persona y el año actual,
# calcule su edad actual y su edad en 10 años.

from datetime import date
from datetime import datetime

nacimiento = int(input(f"Introduzca su año de nacimiento \n-> "))

now = datetime.now()
format = now.strftime("%Y")
edad_actual = int(format)
edad_actual -= nacimiento
edad_futura = edad_actual + 10

print(f"Su edad actual es de {edad_actual}. \nSu edad dentro de 10 años es {edad_futura:.0f}.")
