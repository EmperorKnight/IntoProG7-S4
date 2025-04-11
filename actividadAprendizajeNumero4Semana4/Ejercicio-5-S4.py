# Dado un total de cuenta y un porcentaje de propina (por ejemplo, 10%), calcula cuánto
# dejar de propina.

print(" ")
total_cuenta = float(input(f"Introduzca el total de la cuenta \n-> "))
porcentaje_cuenta = float(input(f"Introduzca el porcentaje de propina \n-> "))

total_propina = (porcentaje_cuenta / 100) * total_cuenta

print(" ")
print(f"La propina a pagar es de C${total_propina:,.2f}")
print(" ")