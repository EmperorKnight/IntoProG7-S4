# Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio

edad = int(input(f" \nIntroduzca su edad \n-> "))

numero_pulsaciones = (220 - edad)/10

print(f" \nEl numero de pulsaciones que una persona es capaz de realizar en 10 segundos de ejercicio es de {numero_pulsaciones:,.1f}\n ")