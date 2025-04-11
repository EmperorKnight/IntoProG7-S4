# Pide una edad actual y muestra qué edad tendrá el usuario dentro de 5, 10 y 20 años

from datetime import datetime

edad_actual = int(input(f" \nIntroduzca su edad actual \n-> "))

actualidad = datetime.now()
actualidad2 = actualidad.strftime("%Y")
hoy = int(actualidad2)

edad_a_5_años = edad_actual + 5
edad_a_10_años = edad_actual + 10
edad_a_20_años = edad_actual + 20

actualidad_dentro_5_años = hoy + 5
actualidad_dentro_10_años = hoy + 10
actualidad_dentro_20_años = hoy + 20

print(f" \nSu edad dentro de 5 años es de {edad_a_5_años} en el año {actualidad_dentro_5_años}")
print(f"Su edad dentro de 10 años es de {edad_a_10_años} en el año {actualidad_dentro_10_años}")
print(f"Su edad dentro de 20 años es de {edad_a_20_años} en el año {actualidad_dentro_20_años} \n ")
