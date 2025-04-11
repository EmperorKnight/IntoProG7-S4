# Diseñe un algoritmo que lea los datos necesarios y calcule la masa

presion = float(input(f" \nIntroduzca la presion para calcular la masa \n-> "))
volumen = float(input(f"Introduzca el volumen para calcular la masa \n-> "))
temperatura = float(input(f"Introduzca la temperatura para calcula la masa \n-> "))

masa = (presion * volumen)/(0.37 * (temperatura + 460))

print(f" \nLa masa es {masa:,.2f} \n ")